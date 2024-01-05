from astropy.io import fits

with fits.open("../figures/fits/mosaic.fits") as hdul:
    header = hdul[0].header  # Assuming the header is in the primary HDU

    # Access specific keywords
    keyword_value = header['MAGZPT']
    keyword_value2 = header['MAGZRR']


# Do something with the keyword_value
print(f'The value of MAGZPT is: {keyword_value}')
print(f'The value of MAGZRR is: {keyword_value2}')