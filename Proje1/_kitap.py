from PyQt6.QtWidgets import *
from kitap import Ui_Form
import sqlite3 ## db dahil ettik
from _arama import Form_Ara

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        ## araçlara erişim değişkeni tanımladık
        self.ktp = Ui_Form()
        self.ktp.setupUi(self) # Ui_Form içindeki başlangıç metodunu çalıştır
        ## Buton tıklanma olayları
        self.ktp.btn_cikis.clicked.connect(self.kapat)
        self.ktp.btn_ekle.clicked.connect(self.ekle)
        self.ktp.btn_listele.clicked.connect(self.listele)
        
        ## Ortak tanımlama blogu
        self.adi = self.ktp.txt_adi  # Zorunlu alan olarak tanımlayacağız
        self.yil = self.ktp.dateEdit_yili
        self.sayfa = self.ktp.spinBox_sayfa
        self.dili = self.ktp.comboBox_dili
        self.yayinevi = self.ktp.comboBox_yayinevi
        self.aciklama = self.ktp.txt_aciklama
    
    def listele(self):
        self.ara = Form_Ara()
        self.ara.show() ## Ara Formunu Göster
              
    ## database oluşturma metodu
    def baglan(self):
        with sqlite3.connect("./kitaplik.db") as veri:
            komut = veri.cursor()
            komut.execute(""" CREATE TABLE IF NOT EXISTS TBL_KITAP 
                        (IDNO INTEGER PRIMARY KEY AUTOINCREMENT,
                        ADI TEXT NOT NULL, YIL TEXT, SAYFA INT, 
                        DILI TEXT, YAYINEVI TEXT, ACIKLAMA TEXT)  """)
            return veri
    
    ## kitap ekleme metodu
    def ekle(self):
        try:
            if self.adi.text() == "":
                QMessageBox.critical(self, "Hata", "Kitap Adı Boş Geçilemez")
            else:
                veri = self.baglan() # baglan metodunda db kontrolunu yap
                komut = veri.cursor()
                
                komut.execute(f""" INSERT INTO TBL_KITAP 
                              (ADI, YIL, SAYFA, DILI, YAYINEVI, ACIKLAMA)
                              VALUES
                              ("{self.adi.text()}", "{self.yil.text()}",
                               {self.sayfa.value()}, "{self.dili.currentText()}",
                               "{self.yayinevi.currentText()}",
                               "{self.aciklama.toPlainText()}")  """)
                
                
                veri.commit() # DB değişikliği olduğu için onayladık
                QMessageBox.information(self, "Kayıt İşlemi", "Kayıt Başarılı")
        except Exception as hata_kodu:
            QMessageBox.warning(self, "Hata", "Bir Hata Oluştu" + str(hata_kodu))
            
        
        
        
    
    def kapat(self):
        yanit = QMessageBox.question(self, "Çıkış İşlemi",
        "Program Kapatılacak. Emin Misin?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        ## yanita göre programı sonlandırsın
        if yanit == QMessageBox.StandardButton.Yes : quit()