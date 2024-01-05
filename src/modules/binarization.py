"""
Converts a fits image from continuous magnitude to binary to simplify object
extraction.
"""
import numpy as np 
from copy import deepcopy

def to_binary(image: np.ndarray, cutoff_brightness: float):
    """
    Converts an image (numpy.ndarray) into a binary format given the threshold
    brightness.
    """
    binary_image = deepcopy(image)
    
    binary_image[image >= cutoff_brightness] = 1
    binary_image[image < cutoff_brightness] = 0

    return binary_image