from astropy.io import fits
from modules.ccl import object_extremes

image_path = "../figures/fits/mosaic_binary.fits"
output_path = "../figures/objects.txt"
with fits.open(image_path) as hdul:
    image = hdul[0].data    
all_extremes = object_extremes(image)   


# Outputing object data to objects.txt file
with open(output_path, "w") as file:
    row_str = "\t".join(["Number", "xmin", "xmax", "ymin", "ymax"])
    file.write(row_str + "\n") 

    for i in range(len(all_extremes)):
        row_str = "\t".join([str(i+1), str(all_extremes[i]["xmin"]), 
                             str(all_extremes[i]["xmax"]), str(all_extremes[i]["ymin"]), 
                            str(all_extremes[i]["ymax"])])
        file.write(row_str + "\n")  


