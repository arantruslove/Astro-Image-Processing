from hans_scripts.crop import crop2
from astropy.io import fits


# Cropping 130 pixels around the edge off
crop2(130,2560-130,130,4611-130,"../figures/fits/mosaic.fits",
      "../figures/fits/border_cropped.fits")

with fits.open("../figures/fits/border_cropped.fits") as hdul:
        data = hdul[0].data


for i in range(4351):
    for j in range(2300):
        if (j>2218 and i>4082) or (j>2037 and i>4283) or (j<65 and i<275) or (j<276 and i<70):
            data[i][j] = 3306  #value is min brightness value of image, obtained from min_value.py

hdu = fits.PrimaryHDU(data)
hdu.writeto("../figures/fits/final_cropped.fits",overwrite=True)