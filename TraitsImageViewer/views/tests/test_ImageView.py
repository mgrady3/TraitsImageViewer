import sys
import unittest

import numpy as np
from PyQt5 import QtWidgets
import pyqtgraph as pg

from TraitsImageViewer.models.ImageModel import ImageModel
from TraitsImageViewer.views.ImageView import (
    ImageView, gen_test_model_random2D
)

app = QtWidgets.QApplication([])

class ImageViewTest(unittest.TestCase):

    def setUp(self):
        self.view = pg.GraphicsView()

    def test_view_random2D(self):
        # given
        im = gen_test_model_random2D()

        # when
        self.imv = ImageView(parent=self.view, model=im)
        self.view.setCentralWidget(self.imv)

        # then
        self.view.show()


if __name__ == '__main__':
    ivt = ImageViewTest()
    ivt.setUp()
    ivt.test_view_random2D()
    sys.exit(app.exec_())