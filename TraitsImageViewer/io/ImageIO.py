"""
Basic I/O functionality for reading and writing image files.

Image I/O uses the PIL (pillow) library for common image formats, but can
also read and write raw data (.dat files).
"""

import numpy as np
from PIL import Image
from TraitsImageViewer.models.ImageModel import ImageModel


def load_image_from_file_PIL(path):
    try:
        im = Image.open(path)
    except:
        # TODO fill in appropriate I/O errors
        pass
    data = np.array(im)
    # print("Loaded Data: shape - {} ndim - {}".format(data.shape, data.ndim))

    if data.ndim == 2:
        cd = 1  # greyscale
    elif data.ndim == 3 and data.shape[2] == 3:
        cd = 3  # RGB 
    elif data.ndim == 3 and data.shape[2] == 4:
        cd = 4  # RGBA or ARGB
    else:
        # TODO: Handle invalid ndim
        return None
    return ImageModel(
        color_depth=cd,
        data=data, 
        height=data.shape[0], 
        width=data.shape[1] 
    )