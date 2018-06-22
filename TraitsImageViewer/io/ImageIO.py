"""
Basic I/O functionality for reading and writing image files.

Image I/O uses the PIL (pillow) library for common image formats, but can
also read and write raw data (.dat files).
"""

import numpy as np
from PIL import Image


def load_image_from_file_PIL(path):
    try:
        im = Image.open(path)
    except:
        # TODO fill in appropriate I/O errors
        pass
    
