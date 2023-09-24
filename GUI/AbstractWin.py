from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QLabel,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget,
    QFileDialog,
    QInputDialog
)


class AbstractWindow(QMainWindow):
    """This Window class is built for base layout setting (select files)"""

    # The key stands for the language shortname, and the value - for the filetype prompt
    __filetypes = {
        "py": "Python (*.py)",
        "c#": "C# (*.cs)",
        "php": "PHP (*.php)",
        # todo: more?
    }
    selected_file = []

    def __init__(self, app_name: str = "Abstract App", lang: str = "py"):
        self.__lang_validate(lang)
        super(AbstractWindow, self).__init__()
        self.lang = lang
        self.setWindowTitle(app_name)
        self.layout = QGridLayout()

    def __lang_validate(self, lang: str) -> None:
        """:raise ValueError:"""
        if lang not in self.__filetypes.keys():
            raise ValueError(f"Incorrect language shortname: {lang}")

    def _select_file(self) -> None:
        file_widget = QFileDialog(self)
        file_widget.setNameFilter(self.__filetypes[self.lang])
        file_widget.setViewMode(QFileDialog.ViewMode.Detail)
        if file_widget.exec():
            filenames = file_widget.selectedFiles()
            self.selected_file = filenames
            self._output_file()

    def _output_file(self) -> None:
        # print(self.selected_file)  # For debugs :33
        filepath_box = QInputDialog(self)
        filepath_box.setDisabled(True)
        filepath_box.setOption(QInputDialog.InputDialogOption.NoButtons)
        filepath_box.setLabelText(None)
        filepath_box.setTextValue(''.join(self.selected_file))
        self.layout.addWidget(filepath_box, 1, 0, alignment=Qt.AlignmentFlag.AlignTop)

    def _calculate(self) -> None:
        """Kinda abstract method OwO"""
        pass

    def set_select_file(self):
        select_file_btn = QPushButton("Select the file")
        select_file_btn.clicked.connect(self._select_file)
        self.layout.addWidget(select_file_btn, 2, 0, alignment=Qt.AlignmentFlag.AlignJustify)

    def set_calculate(self):
        calculate_btn = QPushButton("Estimate metrics!")
        font = calculate_btn.font()
        font.setBold(True)
        font.setPointSize(12)
        calculate_btn.setFont(font)
        calculate_btn.clicked.connect(self._calculate)
        self.layout.addWidget(calculate_btn, 1, 1, alignment=Qt.AlignmentFlag.AlignJustify)

    def set_layout(self) -> None:
        """Sets the final app layout"""
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

