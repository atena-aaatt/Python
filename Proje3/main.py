from PyQt6.QtWidgets import QApplication
from _form import Form

uyg = QApplication([])
pen = Form()
pen.show()
uyg.exec()