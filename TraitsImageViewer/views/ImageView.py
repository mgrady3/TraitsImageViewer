import os
import os.path as op
import numpy as np
import pyqtgraph as pg
from PyQt5 import QtWidgets
import sys

import TraitsImageViewer as TIV
from TraitsImageViewer.models.ImageModel import ImageModel
from TraitsImageViewer.io.ImageIO import load_image_from_file_PIL


class ImageView(pg.PlotItem):
    """ Wrapper around pg.RawImageWidget to use custom ImageModel."""

    def __init__(self, parent=None, model=None):
        super().__init__()
        self.model = model
        self.image = pg.ImageItem(self.model.data)
        self.addItem(self.image)
        # self.setImage(self.model.data)


# View Tests / Utility methods

def gen_test_model_random2D():
    test_data = np.random.randint(0, 2**16 -1, (512, 512)).astype(np.int64)
    return ImageModel(
        color_depth=1,
        data=test_data,
        height=test_data.shape[0],
        width=test_data.shape[1],
    )

def gen_test_model_random3D_RGB():
    # 250 512x512 images stored in RGB ---> 250x3=750
    # Total array size (512, 512, 750) 
    test_data = np.random.randint(0,
                                  2**16 -1,
                                  (512, 512, 750)).astype(np.int64)
    return ImageModel(
        color_depth=3,
        data=test_data,
        height=test_data.shape[0],
        width=test_data.shape[1],
    )

def gen_test_model_random3D_RGBA():
    # 250 512x512 images stored in RGBA ---> 250x4=1000
    # Total array size (512, 512, 1000) 
    test_data = np.random.randint(0,
                                    2**16 -1,
                                    (512, 512, 1000)).astype(np.int64)
    return ImageModel(
        color_depth=4,
        data=test_data,
        height=test_data.shape[0],
        width=test_data.shape[1],
    )

def gen_test_model_actual_image_BW():
    image_path = op.realpath(op.join(TIV.__file__,
                                         os.pardir,
                                         "test_data",
                                         "ozark-mountains-bw.jpg"))
    return load_image_from_file_PIL(image_path)
