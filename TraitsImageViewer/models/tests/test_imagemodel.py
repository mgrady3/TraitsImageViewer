# cSpell:disable
import numpy as np
from numpy.testing import assert_array_equal
import random

import pytest

from TraitsImageViewer.models.ImageModel import ImageModel, ImageStack

class TestImageModel(object):

    def test_image_creation(self):
        # given
        test_data = np.random.randint(0, 2**16 - 1, (512, 512))

        # when
        im = ImageModel(
            color_depth=1,
            data=test_data,
            height=test_data.shape[0],
            width=test_data.shape[1],
        )
        
        # then
        assert isinstance(im.data, np.ndarray)
        assert im.height == im.data.shape[0]
        assert im.width == im.data.shape[1]

    def test_get_data(self):
        # given
        test_data = np.random.randint(0, 2**16 -1, (512, 512))
        im = ImageModel(
            color_depth=1,
            data=test_data,
            height=test_data.shape[0],
            width=test_data.shape[1],
        )

        # when
        result = im.get_data()
        result_t = im.get_data(transpose=True)
        # then
        assert result is im.data
        assert_array_equal(result_t, np.transpose(im.data))


class TestImageStack(object):
    
    def test_imagestack_creation(self):
        # given
        test_data = np.random.randint(0, 2**16 - 1, (512, 512, 250))

        # when 
        ims = ImageStack(
            color_depth=1,
            current_image_index=0,
            data=test_data,
            depth=test_data.shape[2],
            height=test_data.shape[0],
            width=test_data.shape[1],
        )

        # then
        assert ims.color_depth == 1
        assert isinstance(ims.data, np.ndarray)
        assert ims.depth == ims.data.shape[2]
        assert ims.height == ims.data.shape[0]
        assert ims.width == ims.data.shape[1]

    def test_get_data(self):
        # given
        test_data = np.random.randint(0, 2**16 - 1, (512, 512, 250))
        # when
        ims = ImageStack(
            color_depth=1,
            current_image_index=0,
            data=test_data,
            depth=test_data.shape[2],
            height=test_data.shape[0],
            width=test_data.shape[1],
        )

        # then
        assert_array_equal(ims.data, test_data)

    def test_get_current_image(self):
        # given
        test_data = np.random.randint(0, 2**16 - 1, (512, 512, 250))
        index = random.randint(0, test_data.shape[2] - 1)
        ims = ImageStack(
            color_depth=1,
            current_image_index=0,
            data=test_data,
            depth=test_data.shape[2],
            height=test_data.shape[0],
            width=test_data.shape[1],
        )

        # when
        ims.current_image = ImageModel(
            color_depth=1,
            data=test_data[:, :, index],
            height=test_data.shape[0],
            width=test_data.shape[1],
        )

        # then
        assert_array_equal(ims.get_current_image(), ims.current_image)


    def test_get_image(self):
        # given
        test_data = np.random.randint(0, 2**16 - 1, (512, 512, 250))
        index = random.randint(0, test_data.shape[2] - 1)
       
        # when
        ims = ImageStack(
            color_depth=1,
            current_image_index=0,
            data=test_data,
            depth=test_data.shape[2],
            height=test_data.shape[0],
            width=test_data.shape[1],
        )

        # then
        assert_array_equal(ims.get_image(index).data, ims.data[:, :, index])


    def test_valid_index(self):
        # given
        test_data = np.random.randint(0, 2**16 - 1, (512, 512, 250))

        # when 
        ims = ImageStack(
            color_depth=1,
            current_image_index=0,
            data=test_data,
            depth=test_data.shape[2],
            height=test_data.shape[0],
            width=test_data.shape[1],
        )

        check_index_zero = ims.valid_index(0)
        check_index_max = ims.valid_index(ims.depth - 1)
        neg_index_should_fail = ims.valid_index(-1)
        index_too_big_should_fail = ims.valid_index(ims.depth)

        # then
        assert check_index_zero
        assert check_index_max
        assert not neg_index_should_fail
        assert not index_too_big_should_fail
    
