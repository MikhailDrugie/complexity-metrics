import sys
from PyQt6.QtWidgets import QApplication
from gui import HalsteadWin

app = QApplication(sys.argv)
window = HalsteadWin()
window.show()

app.exec()
