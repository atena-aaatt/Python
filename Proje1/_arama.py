from PyQt6.QtWidgets import *
from arama import Ui_Form_Ara
import sqlite3 ## db dahil ettik

class Form_Ara(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ara = Ui_Form_Ara()
        self.ara.setupUi(self)
        self.listele()
    
    ## Aynı veritabanına bağlandık
    def baglan(self):
        with sqlite3.connect("./kitaplik.db") as veri:
            komut = veri.cursor()
            komut.execute(""" CREATE TABLE IF NOT EXISTS TBL_KITAP 
                        (IDNO INTEGER PRIMARY KEY AUTOINCREMENT,
                        ADI TEXT NOT NULL, YIL TEXT, SAYFA INT, 
                        DILI TEXT, YAYINEVI TEXT, ACIKLAMA TEXT)  """)
            return veri
    
    def listele(self):
        tablo = self.ara.tableWidget
        tablo.clear()  # önceden içeriğinde veri varsa üzerine yazmasını engelledik
        try:
            kolonlar = ["IDNO","ADI","KISA TARİH","SAYFA",
                        "DILI","YAYINEVI","ACIKLAMA"]
            # Sütun başlığını kolonlardaki değer olarak ata
            tablo.setHorizontalHeaderLabels(kolonlar)
            veri = self.baglan()
            komut = veri.cursor()
            komut.execute("select * from TBL_KITAP")
            kitaplar = komut.fetchall() ## tüm kayıtları kitaplar değikenine ata
            
            ## Kitaplar değişkeninin içi dolu mu kontrol et
            if kitaplar:
                tablo.setRowCount(len(kitaplar)) # kayıt sayısı kadar satır oluştur
                kitapSayisi = 0
                
                for kitap in kitaplar:
                    tablo.setItem(kitapSayisi, 0, QTableWidgetItem(str(kitap[0])))
                    tablo.setItem(kitapSayisi, 1, QTableWidgetItem(str(kitap[1])))
                    tablo.setItem(kitapSayisi, 2, QTableWidgetItem(str(kitap[2])))
                    tablo.setItem(kitapSayisi, 3, QTableWidgetItem(str(kitap[3])))
                    tablo.setItem(kitapSayisi, 4, QTableWidgetItem(str(kitap[4])))
                    tablo.setItem(kitapSayisi, 5, QTableWidgetItem(str(kitap[5])))
                    tablo.setItem(kitapSayisi, 6, QTableWidgetItem(str(kitap[6])))
                    kitapSayisi += 1
            else:
                QMessageBox.warning(self, "Listeleme Boş","Tabloda Veri Bulunamadı")
            
        except Exception as hatakodu:
            QMessageBox.warning(self, "Listeleme Hatası",
                        "Bir Hata Oluştu" + str(hatakodu))
        