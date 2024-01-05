from astropy.io import fits
import numpy as np
from modules.binarization import to_binary

image_path = "../figures/fits/final_cropped.fits"
output_path = "../figures/fits/bloomed_binary.fits"
with fits.open(image_path) as hdul:
        image = hdul[0].data 

# Creating a binary image for all pixels above he 35000 (blooming) threshold
bloomed_binary = to_binary(image, 35808)


# Calculating the number of experienced above the threshold
count = 0
for pixel in np.nditer(bloomed_binary):
    if pixel == 1:
        count += 1

hdu = fits.PrimaryHDU(bloomed_binary)
hdu.writeto(output_path, overwrite=True)

