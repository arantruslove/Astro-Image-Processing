import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

image_path = "../../images/mosaic.fits"

with fits.open(image_path) as hdul:
        image = hdul[0].data 


# X direction
x_std = []
x_coords = []
for i in range(len(image[0])):
    x_std.append(np.std(image[i]))
    x_coords.append(i)

plt.figure("X direction")
plt.scatter(x_coords,x_std)
plt.xlabel("x position")
plt.ylabel("y position")
plt.show()

