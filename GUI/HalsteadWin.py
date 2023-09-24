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

    def __init__(self, lang: str = "py"):
        super(MainWindow, self).__init__(app_name="Halstead's complexity metrics", lang=lang)

        self.set_select_file()
        self.set_calculate()

        self.set_layout()

