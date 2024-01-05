from astropy.io import fits

def centre_crop(x_centre: float, y_centre: float, width: float, height: float, 
            input_path: str, output_path: str) -> None:
    """Crops a fit file and outputs the cropped fitfile."""

    with fits.open(input_path) as hdul:
        data = hdul[0].data 

    x1 = int(round(x_centre - width/2))
    x2 = int(round(x_centre + width/2))
    y1 = int(round(y_centre - height/2))
    y2 = int(round(y_centre + height/2))

    # Extract the subimage
    subimage = data[y1:y2, x1:x2]

    # Save the subimage to a new FITS file
    hdu = fits.PrimaryHDU(subimage)
    hdu.writeto(output_path, overwrite=True)


def edge_crop(x_start:int,x_end:int,y_start:int,y_end:int,input_path:str,
              output_path:str)->None:
    with fits.open(input_path) as hdul:
        data = hdul[0].data
    cropped_image = data[y_start:y_end,x_start:x_end]
    hdu = fits.PrimaryHDU(cropped_image)
    hdu.writeto(output_path,overwrite=True)

