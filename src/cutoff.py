from astropy.io import fits
import math

image_path = "../figures/fits/final_cropped.fits"
with fits.open(image_path) as hdul:
        image = hdul[0].data 

pixel_count = 0
count_count = 0
for row in image:
        for element in row:
            if element < 3450:  #blooming count
                pixel_count +=1
                count_count += element

with open('../figures/objects.txt', 'r') as file:
    lines = file.readlines()

    xmin = []
    xmax = []
    ymin = []
    ymax = []

    for line in lines[1:]:
        columns = line.split()
        xmin.append(float(columns[1]))
        xmax.append(float(columns[2]))
        ymin.append(float(columns[3]))
        ymax.append(float(columns[4]))

area_sum =0
for i in range(len(xmin)):
    area_sum += (xmax[i]-xmin[i])*(ymax[i]-ymin[i])

cutoff = 25.3-(2.5*math.log((area_sum/len(xmin))*(count_count/pixel_count),10))



print(cutoff)