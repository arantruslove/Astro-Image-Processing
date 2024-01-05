import numpy as np
from copy import deepcopy
from astropy.io import fits
from scipy.ndimage import gaussian_filter
from skimage.feature import peak_local_max

def find_connected_ones(matrix: np.ndarray, start_x: int, start_y: int) -> np.ndarray:
    matrix_copy = deepcopy(matrix)
    connected_ones = set()
    stack = [(start_x, start_y)]

    while stack:
        x, y = stack.pop()
        if (x < 0 or y < 0 or x >= matrix_copy.shape[0] or y >= matrix_copy.shape[1]
            or matrix_copy[x, y] == 0):
            continue
        connected_ones.add((x, y))
        matrix_copy[x, y] = 0  # Mark as visited
        stack.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

    return np.array(list(connected_ones))


def erase_object(image: np.ndarray, start_x: int, start_y: int) -> None:
    """Erases an object in an image by the position of one of its pixels."""

    # Return all the coordinates of the pixels
    object_pixels = find_connected_ones(image, start_x, start_y)
    for coord in object_pixels:
        image[coord[0]][coord[1]] = 0


def location_of_ones(binary_image: np.ndarray) -> np.ndarray:
    """Given the binary_image data, returns the location of all the 1s."""
    rows, cols = np.where(binary_image == 1)
    locations = np.column_stack((rows, cols))
    return locations


def erase_all_objects(image: np.ndarray, locations_to_remove: np.ndarray) -> None:
        """Removes all objects that have their body on the flagged locations."""
        for location in locations_to_remove:
                erase_object(image, location[0], location[1])


def coord_extremes(coords: np.ndarray) -> dict:
    """
    Finds the extreme x, y coordinates of a numpy array of 2D coordinates and
    returns these extreme coordinates in a dictionary.
    """
    
    map = {}
    x_list = []
    y_list = []
    for coord in coords:
        x_list.append(coord[1])
        y_list.append(coord[0])
    
    map["xmin"] = min(x_list)
    map["xmax"] = max(x_list)
    map["ymin"] = min(y_list)
    map["ymax"] = max(y_list)

    return map


def object_extremes(binary_image: np.ndarray) -> list[dict]:
    """
    Outputs a list of dictionaries that contain information on the coordinate
    boundaries of all the objects in a binary image.
    """
    binary_copy = deepcopy(binary_image)
    rows, columns = binary_copy.shape  # Get the dimensions of the binary image

    all_extremes = []
    for i in range(rows):
        for j in range(columns):
            if binary_copy[i, j] == 1:
                object_coords = find_connected_ones(binary_copy, i, j)
                extremes = coord_extremes(object_coords)
                all_extremes.append(extremes)
                erase_object(binary_copy, i, j)
    
    return all_extremes


def surrounding_brightnesses(image: np.ndarray, xmin: int, xmax: int, ymin: int, ymax: int, 
                             buffer: int) -> np.ndarray:
    """
    Returns a numpy 1D array of pixel brightness of the surrounding pixels of an
    object (located from xmin, xmax, ymin and ymax).
    """
    
    with_borders = image[ymin-buffer:ymax+buffer, xmin-buffer:xmax+buffer]
    
    # Create a mask of the same shape as with_borders, with the region of interest set 
    # to True
    mask = np.zeros(with_borders.shape, dtype=bool)
    mask[buffer:-buffer, buffer:-buffer] = True
    
    # Flatten both the with_borders array and the mask
    flat_values = with_borders.flatten()
    flat_mask = mask.flatten()
    
    return flat_values[~flat_mask]


def determine_count(image:np.ndarray, xmin:int, xmax:int, ymin:int, ymax:int, 
                    first_buffer: int, second_buffer: int, output_image=False) -> int:
        """Determines the count of an object."""

        # Getting the object section
        object = image[ymin-first_buffer:ymax+first_buffer,
                       xmin-first_buffer:xmax+first_buffer]
        mean_brightness = np.mean(object)
        brightness_std = np.std(object)
        upper_bnd = mean_brightness + 1 * brightness_std

        # Finding the background brightness
        surroundings = surrounding_brightnesses(image, xmin, xmax, ymin, ymax,
                                                 second_buffer)
        filtered_surroundings = [brightness for brightness in surroundings if brightness < 
                                upper_bnd]
        background = np.mean(filtered_surroundings)
        background_std = np.std(filtered_surroundings)
        threshold = background + 2 * background_std

        # Subtract background from object brightnesses and find the mean
        brightnesses = [brightness-background for brightness in object.flatten() 
                        if brightness > threshold]
        
        if output_image:
            contrib_object = image[ymin-first_buffer:ymax+first_buffer,
                        xmin-first_buffer:xmax+first_buffer]
            # Thresholding
            contrib_object = np.where(contrib_object > threshold, 1, 0)
            hdu = fits.PrimaryHDU(contrib_object)
            hdu.writeto("../test_figures/objects/binary_object.fits", overwrite=True) 
            print("Image has been output")

        return np.sum(brightnesses)


def is_multi_peak(image:np.ndarray, filter_sigma:int, diag_divider:int, ):
    """Checks if an image has multiple peaks based on parameters."""

    height, width = image.shape
    diagonal = int((width**2 + height**2)**0.5)
    smoothed_image = gaussian_filter(image, sigma=filter_sigma)
    coordinates = peak_local_max(smoothed_image, 
                                 min_distance=diagonal//diag_divider, 
                                 num_peaks=np.inf, exclude_border=False)

    if len(coordinates) > 1:
        return True
    else:
         return False
