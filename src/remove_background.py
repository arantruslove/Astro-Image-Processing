from astropy.io import fits
from skimage import morphology
from modules.pre_processing import subtract_background_by_regions
from modules.classes import CutoffRegion


# Regions
region_1 = CutoffRegion(xmin=0, xmax=1294, ymin=0, ymax=1192, cutoff=3421.0)
region_2 = CutoffRegion(xmin=1295, xmax=2300, ymin=0, ymax=1192, cutoff=3405.0)
region_3 = CutoffRegion(xmin=0, xmax=725, ymin=1193, ymax=3732, cutoff=3419.0)
region_4 = CutoffRegion(xmin=726, xmax=1267, ymin=1193, ymax=2417, cutoff=3416.0)
region_5 = CutoffRegion(xmin=1268, xmax=1798, ymin=1193, ymax=2417, cutoff=3418.0)
region_6 = CutoffRegion(xmin=1799, xmax=2300, ymin=1193, ymax=1586, cutoff=3421.0)
region_7 = CutoffRegion(xmin=1799, xmax=2300, ymin=1587, ymax=2166, cutoff=3414.0)
region_8 = CutoffRegion(xmin=726, xmax=1798, ymin=2418, ymax=3732, cutoff=3429.0)
region_9 = CutoffRegion(xmin=1799, xmax=2300, ymin=2167, ymax=2978, cutoff=3413.0)
region_10 = CutoffRegion(xmin=1799, xmax=2300, ymin=2979, ymax=4051, cutoff=3413.0)
region_11 = CutoffRegion(xmin=0, xmax=1798, ymin=3733, ymax=4051, cutoff=3419.0)
region_12 = CutoffRegion(xmin=0, xmax=2300, ymin=4052, ymax=4351, cutoff=3416.0)

regions = [region_1, region_2, region_3, region_4, region_5, region_6, region_7, 
           region_8, region_9, region_10, region_11, region_12]

image_path = "../figures/fits/final_cropped.fits"
output_path = "../figures/test_fits/mosaic_less_background.fits"
with fits.open(image_path) as hdul:
        image = hdul[0].data 


subtract_background_by_regions(image, regions)
selem = morphology.disk(1)
opened_image = morphology.opening(image, selem)

hdu = fits.PrimaryHDU(opened_image)
hdu.writeto(output_path, overwrite=True)

