import numpy as np
from .classes import CutoffRegion

def subtract_background(image: np.ndarray, background: float) -> None:
    """Function that removes the background from an image."""
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Subtract the background value and clip to zero if negative
            new_value = image[i, j] - background
            if new_value <= 0:
                image[i, j] = 0
            else:
                image[i,j] = new_value


def subtract_background_by_regions(image: np.ndarray, regions: list[CutoffRegion]) -> None:
    """
    Function that removes the background from an image for multiple specified regions.
    """
    for region in regions:
        # Define region indices
        ymin, ymax, xmin, xmax = region.ymin, region.ymax, region.xmin, region.xmax
        
        # Subtract the background value and clip to zero if negative
        subtracted_values = image[ymin:ymax+1, xmin:xmax+1] - region.cutoff
        subtracted_values = np.clip(subtracted_values, 0, None)
        
        # Update the corresponding region in the original image
        image[ymin:ymax+1, xmin:xmax+1] = subtracted_values
