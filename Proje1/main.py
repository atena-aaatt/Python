from PyQt6.QtWidgets import QApplication # derleyici modülü
from _kitap import Form

uygulama = QApplication([])
pencere = Form()
pencere.show()
uygulama.exec()