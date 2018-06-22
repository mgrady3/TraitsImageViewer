# cSpell:disable
import numpy as np
from traits.api import (
    ArrayOrNone, HasTraits, Int, Str
)   


class ImageModel(HasTraits):
    """ Representation of a 2D image using a numpy 2d array."""

    color_depth = Int  # Greyscale, RGB, RGBA
    data = ArrayOrNone  # 2d numpy array
    height = Int
    width = Int


    def get_data(self, transpose=False):
        """ Get image array; optionally return transposed data."""
        if transpose:
            return np.transpose(self.data)
        return self.data
    
class ImageStack(HasTraits):
    """ Representation of a 3D stack of 2D images; (HxWxD)."""

    color_depth = Int # Greyscale, RGB, RGBA
    current_image = ImageModel
    current_image_index = Int
    data = ArrayOrNone  # 3d numpy array
    depth = Int  # Number of images
    height = Int
    width = Int

    def get_current_image(self):
        return self.current_image

    def get_image(self, index):
        if self.valid_index(index):
            return ImageModel(
                color_depth=self.color_depth,
                data=self.data[:, :, index],
                height=self.height,
                width=self.width,
            )
        raise IndexError

    def get_data(self, transpose=False):
        """ Get image array."""
        if transpose:
            return np.transpose(self.data)
        return self.data

    def valid_index(self, index):
        return index in range(self.depth)  # [0, depth - 1]
    


    

    






    