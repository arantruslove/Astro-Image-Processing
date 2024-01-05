"""Outputs all the images from the objects.txt file."""
from astropy.io import fits
from modules.ccl import is_multi_peak

image_path = "../figures/fits/final_cropped.fits"
object_path = "../figures/objects.txt"
output_path = "../figures/objects_filtered.txt"

# Importing the image
with fits.open(image_path) as hdul:
        image = hdul[0].data

# Retained lines (rows that pass the test)
retained_lines = []

with open(object_path, "r") as file:
    header = next(file)
    retained_lines.append(header)
    
    for line in file:

        try:
            # Split the line into individual values based on tabs
            values = line.strip().split('\t')
            
            # Extract and convert the values
            number = int(values[0])
            xmin = int(values[1])
            xmax = int(values[2])
            ymin = int(values[3])
            ymax = int(values[4])
            
            buffer = 6
            xmin_buf = xmin - buffer
            xmax_buf = xmax + buffer
            ymin_buf = ymin - buffer
            ymax_buf = ymax + buffer 

            obj = image[ymin_buf:ymax_buf, xmin_buf:xmax_buf]
            print(xmin_buf)
            
            # Check if the object passes the multi-peak test
            test = is_multi_peak(obj, 1, 5)

            # If it passes, store the line
            if not test:
                retained_lines.append(line)
        except:
             pass

# Writing the retained lines to the output file
with open(output_path, "w") as file:
    file.writelines(retained_lines)
