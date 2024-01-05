"""
Script coverts objects counts to magnitudes by reading data from the objects.txt file.
"""
import math
# Open the text file for reading
with open('../figures/objects_counts.txt', 'r') as file:
    lines = file.readlines()

    # Initialize a list to store the data from the 6th column
    column_six_data = []

    # Skip the first line (header)
    for line in lines[1:]:
        columns = line.split()

        # Extract the data from the 6th column 
        column_six_data.append(columns[5])

for i in range(len(column_six_data)):
    try:
        count =  float(column_six_data[i])
        column_six_data[i] = 25.3-(2.5*math.log(count,10))
    except:
        column_six_data[i] = "error"

# Modify the first line (header) to add the "magnitude" header
lines[0] = lines[0].strip() + " magnitude\n"

# Append the data from the array to the 6th column
for i, line in enumerate(lines[1:]):
    lines[i + 1] = line.strip() + " " + str(column_six_data[i]) + "\n"

# Write the modified lines back to the text file
with open('../figures/objects_magntiude.txt', 'w') as file:
    file.writelines(lines)