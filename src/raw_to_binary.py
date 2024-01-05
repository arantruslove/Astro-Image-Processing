from astropy.io import fits
from modules.binarization import to_binary

# Binarizing the whole image
image_path = "../figures/fits/no_blooms_mosaic.fits"
output_path = "../figures/fits/mosaic_binary.fits"

with fits.open(image_path) as hdul:
        image = hdul[0].data 

binary_image = to_binary(image, 18.4)

# Save the subimage to a new FITS file
hdu = fits.PrimaryHDU(binary_image)
hdu.writeto(output_path, overwrite=True)