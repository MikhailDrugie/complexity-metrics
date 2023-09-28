from . import AbstractWindow
from factories import HalsteadFactory


class MainWindow(AbstractWindow):

    def __init__(self):
        super(MainWindow, self).__init__(app_name="Halstead's complexity metrics")
        self._factory = HalsteadFactory()

        self.set_basic()
        self.set_layout()
