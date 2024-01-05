"""Script that creates a sample from the main image."""

from astropy.io import fits

with fits.open("../figures/fits/final_cropped.fits") as hdul:
        image = hdul[0].data 

# Number: 4088
xmin = 2254
xmax = 2269
ymin = 3576
ymax = 3596
buffer = 6
image_section = image[ymin-buffer:ymax+buffer,xmin-buffer:xmax+buffer]


print(image_section)
hdu = fits.PrimaryHDU(image_section)
hdu.writeto("../test_figures/objects/test_object.fits", overwrite=True)