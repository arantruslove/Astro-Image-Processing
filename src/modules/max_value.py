from astropy.io import fits

def max_value(file:str) -> int:
    with fits.open(file) as hdul:
        data = hdul[0].data
    max_value = 0
    for row in data:
        for element in row:
            if element > max_value:
                max_value = element
    return max_value