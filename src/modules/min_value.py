from astropy.io import fits

with fits.open("../../figures/fits/cropped.fits") as hdul:
        data = hdul[0].data

min_value = float("inf")
for row in data:
    for element in row:
        if element < min_value:
            min_value = element
print(min_value)