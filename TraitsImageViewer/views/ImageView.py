import numpy as np
import pyqtgraph as pg
from PyQt5 import (
    QtCore, QtGui, QtWidgets,
)
import sys

from TraitsImageViewer.models.ImageModel import ImageModel


class ImageView(pg.PlotItem):
    """ Wrapper around pg.RawImageWidget to use custom ImageModel."""

    def __init__(self, parent=None, model=None):
        super().__init__()
        self.model = model
        self.image = pg.ImageItem(self.model.data)
        self.addItem(self.image)
        # self.setImage(self.model.data)


# View Tests

def gen_test_model_random2D():
    test_data = np.random.randint(0, 2**16 -1, (512, 512)).astype(np.int64)
    return ImageModel(
        color_depth=1,
        data=test_data,
        height=test_data.shape[0],
        width=test_data.shape[1],
    )

def main():
    app = QtGui.QApplication([])

    # win = QtWidgets.QMainWindow()
    # win.setWindowTitle("Traits-ImageViewer")
   
    view = pg.GraphicsView()
    im = gen_test_model_random2D()
    imv = ImageView(parent=view, model=im)
    view.setCentralWidget(imv)
    # win.setCentralWidget(imv)
    # win.show()
    view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
