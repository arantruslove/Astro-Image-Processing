import numpy as np 
from astropy.io import fits

def background(x1:int,y1:int,x2:int,y2:int)->int:
    with fits.open("../figures/fits/final_cropped.fits") as hdul:
        data = hdul[0].data 
    subimage = data[y1:y2, x1:x2]
    background = np.median(subimage)
    return background