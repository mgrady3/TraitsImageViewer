# cSpell:disable
import numpy as np
from numpy.testing import assert_array_equal
import os
from os import path as op

import pytest

import TraitsImageViewer as TIV
import TraitsImageViewer.io.ImageIO as imio

class TestImageIO(object):

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
        
    def test_load_image_RGBA_PIL(self):
         # given
        image_path = op.realpath(op.join(TIV.__file__,
                                         os.pardir,
                                         "test_data",
                                         "AlphaBall.png"))
        # when
        im = imio.load_image_from_file_PIL(image_path)

        # then
        assert isinstance(im, TIV.models.ImageModel.ImageModel)
        assert im.color_depth == 4  # RGBAGreyscale image
        assert im.data.ndim == 3

    def test_load_image_from_file_raw_2D(self):
        # given
        image_path = op.realpath(op.join(TIV.__file__,
                                         os.pardir,
                                         "test_data",
                                         "test-LEEM.dat"))
        ht = 600
        wd = 592
        bits = 16
        byte_order = 'L'

        # when
        image = imio.load_image_from_file_raw_2D(path=image_path,
                                                 ht=ht,
                                                 wd=wd,
                                                 bits=bits,
                                                 byte_order=byte_order
                                                )

        # then
        assert isinstance(image, np.ndarray)
        assert image.ndim == 2
        assert image.shape == (ht, wd)
