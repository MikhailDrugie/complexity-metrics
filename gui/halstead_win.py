from . import AbstractWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QFileDialog
)


class MainWindow(AbstractWindow):

    def __init__(self):
        super(MainWindow, self).__init__(app_name="Halstead's complexity metrics")

        self.set_basic()

        self.set_layout()