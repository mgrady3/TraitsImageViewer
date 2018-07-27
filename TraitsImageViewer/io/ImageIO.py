"""
Basic I/O functionality for reading and writing image files.

Image I/O uses the PIL (pillow) library for common image formats, but can
also read and write raw data (.dat files).
"""

import numpy as np
import os
from PIL import Image
from TraitsImageViewer.models.ImageModel import ImageModel, ImageStack


class InvalidParameterError(Exception):
    """Indicate that required params for parsing data files are not present."""

    def __init__(self, message=None):
        if message is None:
            message = "Error: Invalid or Insufficient Parameters required to process data files."
        super(InvalidParameterError, self).__init__(message)

class FormatNotSupportedError(Exception):
    """ Indicate that image format is not supported."""

    def __init__(self, message=None):
        if message is None:
            message = "Error: Requested image format is not yet supported."
        super(InvalidParameterError, self).__init__(message)


def load_image_from_file_PIL(path):
    """ Generate ImageModel from file using PIL.Image.open()."""
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

def load_image_from_file_raw_2D(path, ht=None, wd=None, 
                                bits=None, byte_order=None):
    """ Load .dat file into 2D numpy array.

    :param path: string path to file
    :param ht: integer pixel height of image
    :param wd: integer pixel width of image
    :param bits: integer representing bit depth of image, i.e. bits per pixel - 
        default is 16 bit
    :param byte_order: string representing byte order,
        'L' for Little-Endian (Intel), 
        'B' for Big-Endian (Motorola)
    :return dat_arr: 2D numpy array
    """
    # ensure all params are not None
    if (not ht and wd and bits and byte_order) or not os.path.exists(path):
        raise InvalidParameterError

    if not bits % 8 == 0:
        raise InvalidParameterError

    bits_per_byte = 8
    
    if bits == 8 and byte_order == 'L':
        formatstring = '<u1'  # 1 byte (8 bits) per pixel
    elif bits == 8 and byte_order == 'B':
        formatstring = '>u1'

    elif bits == 16 and byte_order == 'L':
        formatstring = '<u2'  # 2 bytes (16 bits) per pixel
    elif bits == 16 and byte_order == 'B':
        formatstring = '>u2'
    elif bits > 16 or byte_order not in ['L', 'B']:
        raise FormatNotSupportedError
    
    # read file, discard header info, convert image data into numpy array
    with open(path, 'rb') as f:
        header_length = len(f.read()) - (int(bits/bits_per_byte) * ht * wd)
        f.seek(0)
        return np.fromstring(f.read()[header_length:],
                                formatstring).reshape((ht, wd))
    
def load_image_stack(image_type, **kwargs):
    if not image_type.lower() in ('raw', 'image'):
        raise InvalidParameterError
    if image_type.lower() == 'raw':
        return self.load_image_stack_raw(**kwargs)    
    return self.load_image_stack_PIL(**kwargs)

def load_image_stack_raw(**kwargs):
    """ Load 3D Image Stack from raw data files.

    :param path: str to directory containing files to load
    :param ext: str file extension
    :param width: int image width
    :param height: int image height
    :param bits: int bits per pixel
    :param byte_order: str byte_order of data ('L' or 'M')

    :return ims: TraitsImageViewer.models.ImageModel.ImageStack
    """
    path = kwargs['path']
    ext = kwargs['ext']
    files = sorted([name for name in os.listdir(path)
                         if name.endswith(ext)])
    arrays = []
    for fl in files:
        im_data = load_image_from_file_raw_2D(path=os.path.join(path, fl),
                                              ht=kwargs['height'],
                                              wd=kwargs['width'],
                                              bits=kwargs['bits'],
                                              byte_order=kwargs['byte_order']
                                              )
        arrays.append(im_data)
    arrays = np.dstack(arrays)
    return ImageStack(color_depth=1,
                      data=arrays,
                      depth=arrays.shape[2],
                      height=arrays.shape[0],
                      width=arrays.shape[1])
        


def load_image_stack_PIL(**kwargs):
    """ Load 3D Image Stack using PIL.Image.Open
    
    :param path: str to directory containing files to load
    :param ext: str file extension

    :return ims: TraitsImageViewer.models.ImageModel.ImageStack
    """
    pass




