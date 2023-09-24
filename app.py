import sys
from PyQt6.QtWidgets import QApplication
from GUI import HalsteadWin

app = QApplication(sys.argv)
window = HalsteadWin()
window.show()

app.exec()
