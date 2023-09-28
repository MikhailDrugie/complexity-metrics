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

    def _calculate(self) -> None:
        if not self._file_select_validate():
            self._file_not_selected_msg()
            return
        with open(self.selected_file[0]) as code_file:
            code = code_file.read()
