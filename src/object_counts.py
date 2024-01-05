"""Outputs all the images from the objects.txt file."""
from astropy.io import fits
from modules.ccl import determine_count

image_path = "../figures/fits/final_cropped.fits"
object_path = "../figures/objects_filtered.txt"
output_path = "../figures/objects_counts.txt"

# Importing the image
with fits.open(image_path) as hdul:
        image = hdul[0].data


# Initialize empty lists to store data
numbers = []
xmin_values = []
xmax_values = []
ymin_values = []
ymax_values = []

# Open the .txt file for reading
with open(object_path, "r") as file:
    # Skip the header line
    next(file)
    
    # Loop through each line in the file
    for line in file:
        # Split the line into individual values based on tabs
        values = line.strip().split('\t')
        
        # Convert the values to appropriate data types if needed
        number = int(values[0])
        xmin = int(values[1])
        xmax = int(values[2])
        ymin = int(values[3])
        ymax = int(values[4])
        
        # Append the values to their respective lists
        numbers.append(number)
        xmin_values.append(xmin)
        xmax_values.append(xmax)
        ymin_values.append(ymin)
        ymax_values.append(ymax)

buffer = 0
xmin_values = [x - buffer if x >= buffer else 0 for x in xmin_values]
xmax_values = [x + buffer if x <= 2230 - buffer else 2230 for x in xmax_values]
ymin_values = [y - buffer if y >= buffer else 0 for y in ymin_values]
ymax_values = [y + buffer if y <= 2341 - buffer else 4341 for y in ymax_values]

counts = []
for i in range(len(xmin_values)):
    buffer = 6
    xmin = xmin_values[i] - buffer
    xmax = xmax_values[i] + buffer
    ymin = ymin_values[i] - buffer
    ymax = ymax_values[i] + buffer 

    count = determine_count(image, xmin, xmax, ymin, ymax, 6, 10)
    counts.append(count)


# Storing the previous data and counts into a new list
updated_data = []
with open(object_path, "r") as file:
    # Read the header line and add the "counts" column
    header = next(file).strip() + "\tcounts\n"
    updated_data.append(header)
    
    # Loop through each line in the file and add the counts
    for idx, line in enumerate(file):
        updated_line = line.strip() + "\t" + str(counts[idx]) + "\n"
        updated_data.append(updated_line)

# Writing the updated data back to the objects.txt file
with open(output_path, "w") as file:
    file.writelines(updated_data)
