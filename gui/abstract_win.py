from metrics import AbstractMetrics
from factories.abstract import AbstractFactory
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget,
    QFileDialog,
    QInputDialog,
    QComboBox,
    QMessageBox
)


class AbstractWindow(QMainWindow):
    """This Window class is built for base layout setting (select files)"""

    # The key stands for the language shortname, and the value - for the filetype prompt
    __languages: dict = {
        "Python": "py",
        "PHP": "php",
        "C#": "cs",
        # todo: more?
    }
    __filetypes: dict = {
        "py": "Python (*.py)",
        "cs": "C# (*.cs)",
        "php": "PHP (*.php)",
        # todo: more?
    }
    __selected_file: list = []
    lang: str = __languages[list(__languages.keys())[0]]
    _factory: AbstractFactory | None = None

    def __init__(self, app_name: str = "Abstract App"):
        super(AbstractWindow, self).__init__()
        self.setWindowTitle(app_name)
        self.layout = QGridLayout()

    def __short_lang_validate(self, lang: str) -> None:
        """:raise ValueError:"""
        if lang not in self.__filetypes.keys():
            raise ValueError(f"Incorrect language shortname: {lang}")

    def __text_lang_validate(self, text_lang: str) -> None:
        """:raise ValueError:"""
        if text_lang not in self.__languages.keys():
            raise ValueError(f"Incorrect language: {text_lang}")

    def _language_changed(self, text_lang: str):
        self.__text_lang_validate(text_lang)
        self.lang = self.__languages[text_lang]
        self.__short_lang_validate(self.lang)

    def _select_file(self) -> None:
        file_widget = QFileDialog(self)
        file_widget.setNameFilter(self.__filetypes[self.lang])
        file_widget.setViewMode(QFileDialog.ViewMode.Detail)
        if file_widget.exec():
            filenames = file_widget.selectedFiles()
            self.__selected_file = filenames
            self._output_file()

    def _output_file(self) -> None:
        # print(self.__selected_file)  # For debugs :33
        filepath_box = QInputDialog(self)
        filepath_box.setDisabled(True)
        filepath_box.setOption(QInputDialog.InputDialogOption.NoButtons)
        filepath_box.setLabelText(None)
        filepath_box.setTextValue(''.join(self.__selected_file))
        self.layout.addWidget(filepath_box, 1, 0)

    def _validate_selected_file(self):
        return len(self.__selected_file) > 0 and self.__selected_file[0].split('.')[-1] == self.lang

    def __incorrect_selected_file_msg(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Warning!")
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setText("No file selected or file type is incorrect!")
        msg_box.exec()

    def _calculate(self) -> None:
        if not self._validate_selected_file():
            self.__incorrect_selected_file_msg()
            return
        with open(self.__selected_file[0]) as code_file:
            code = code_file.read()
            code_file.close()

        if not self._factory:  # todo: error catch and display!
            print('ok\n-------------------------------------')
            print(code)
            return

        classname = self._factory.get_class(self.lang)
        if classname is None:  # todo: error catch and display!
            print(f"Unknown class for lang {self.lang}!")
            return

        singleton: AbstractMetrics = classname(code=code)

        data = singleton.execute()
        print(data)

    def set_select_language(self):
        dropdown = QComboBox()
        dropdown.addItems(self.__languages.keys())
        dropdown.currentTextChanged.connect(self._language_changed)
        self.layout.addWidget(dropdown, 0, 0)

    def set_select_file(self):
        select_file_btn = QPushButton("Select the file")
        select_file_btn.clicked.connect(self._select_file)
        self.layout.addWidget(select_file_btn, 2, 0)

    def set_calculate(self):
        calculate_btn = QPushButton("Estimate metrics!")
        font = calculate_btn.font()
        font.setBold(True)
        font.setPointSize(12)
        calculate_btn.setFont(font)
        calculate_btn.clicked.connect(self._calculate)
        self.layout.addWidget(calculate_btn, 1, 1)

    def set_basic(self):
        self.set_select_language()
        self.set_select_file()
        self.set_calculate()

    def set_layout(self) -> None:
        """Sets the final app layout"""
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)