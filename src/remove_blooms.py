from astropy.io import fits
from skimage import morphology
from modules.ccl import (location_of_ones, erase_all_objects)

                                

image_path = "../figures/test_fits/mosaic_less_background.fits"
bloomed_path = "../figures/fits/bloomed_binary.fits"
output_path = "../figures/fits/no_blooms_mosaic.fits"

with fits.open(image_path) as hdul:
        image = hdul[0].data

with fits.open(bloomed_path) as hdul:
        bloomed_image = hdul[0].data 

# Erase all the blooming objects
locations_to_remove = location_of_ones(bloomed_image)
erase_all_objects(image, locations_to_remove)


# Remove the residual specks using morphological opening
selem = morphology.disk(1)
opened_image = morphology.opening(image, selem)

hdu = fits.PrimaryHDU(opened_image)
hdu.writeto(output_path, overwrite=True)
        