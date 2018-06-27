# cSpell:disable
import numpy as np
from numpy.testing import assert_array_equal
import os
from os import path as op

import pytest

import TraitsImageViewer as TIV
import TraitsImageViewer.io.ImageIO as imio

class TestImageIO(object):

    def test_load_image_RGB_PIL(self):
        # given
        image_path = op.realpath(op.join(TIV.__file__,
                                         os.pardir,
                                         "test_data",
                                         "ozark-mountains.jpg"))
        # when
        im = imio.load_image_from_file_PIL(image_path)

        # then
        assert isinstance(im, TIV.models.ImageModel.ImageModel)
        assert im.color_depth == 3  # RGB image
        assert im.data.ndim == 3
        assert im.data.shape[2] == 3

    def test_load_image_greyscale_PIL(self):
         # given
        image_path = op.realpath(op.join(TIV.__file__,
                                         os.pardir,
                                         "test_data",
                                         "ozark-mountains-bw.jpg"))
        # when
        im = imio.load_image_from_file_PIL(image_path)

        # then
        assert isinstance(im, TIV.models.ImageModel.ImageModel)
        assert im.color_depth == 1  # Greyscale image
        assert im.data.ndim == 2


