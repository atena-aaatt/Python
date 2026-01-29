from PyQt6.QtWidgets import*
from PyQt6.QtWidgets import QApplication,QLabel
from  kayit import kayit_Form
import sqlite3
from email.message import EmailMessage
import ssl, smtplib
from bilgi import bilgi_Form
from giris import Ui_Form

class kayit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main3 = kayit_Form()
        self.main3.setupUi(self)
        #Değişken tanımlamaları 
        self.epost=self.main3.k_email
        self.adi=self.main3.adi
        self.parola=self.main3.k_sifre
        #Düğmeler
        self.main3.b_k_g.clicked.connect(self.giris)
        self.main3.b_k_uye.clicked.connect(self.kullanici_kayit)
    def giris(self):
            super().__init__()
            self.main2 = Ui_Form()
            self.main2.setupUi(self)
            self.show()
            #Giriş Düğmesi
            self.main2.pushButton_3.clicked.connect(self.listele)
            self.main2.pushButton_2.clicked.connect(self.epostagonder)
            self.main2.b_g_g.clicked.connect(self.oturumac)
            #tanıtım
            self.epost=self.main2.lineEdit
            self.parola=self.main2.lineEdit_2
            self.giris=self.main2.b_g_g
    
    def baglanti(self):
        
        with sqlite3.connect("kullaniciler.db")as baglan:
            komut=baglan.cursor()
            komut.execute(""" CREATE TABLE IF NOT EXISTS tbl_kayit 
                          (EPOSTA TEXT , ADI TEXT, PAROLA TEXT)""")
            return baglan
    def kullanici_kayit(self) :
        try:
            #tanıtım
            self.adi_=self.main3.adi
            self.email=self.main3.k_email
            self.parola2=self.main3.k_sifre
           
            if (self.email.text() != "") and (self.parola2.text() != "")and (self.adi_.text()!=""):
                baglan=self.baglanti()
                komut=baglan.cursor()
                komut.execute(f""" INSERT INTO tbl_kayit VALUES 
                            ("{self.epost.text()}","{self.adi.text()}","{self.parola.text()}")""")
                baglan.commit()
                
                QMessageBox.information(self,"kayıt işlemi","kayıt oldu")
            else:
                QMessageBox.critical(self,("HATA","Bilgileri tamamlayın"))    
        except Exception as hata:
            QMessageBox.critical(self,"uyarı",
                                "hata oluştu \n "+str(hata))    
         
    def oturumac(self):
        try:
           
            if (self.epost.text() != "") or (self.parola.text() != ""):
                baglan = self.baglanti()
                komut = baglan.cursor()
                komut.execute(" select * from tbl_kayit ")
                uyeler = komut.fetchall()
                for uye in uyeler:
                    
                    if (self.epost.text() == uye[0]) and (self.parola.text() == uye[2]):
                        QMessageBox.information(self,"oturumaçti","başarlı")
                        self.hide()
                    else :
                        QMessageBox.information(self,"hata","Bilgiler Doğru Diğil")
            else:
                QMessageBox.critical(self, "Oturum Açma Hatası", "Hatalı Giriş")
        except Exception as hatakodu:
            QMessageBox.critical(self, "HATA", "Bir Hata Oluştu \n"+str(hatakodu))
    
    def user(self):
        
            baglan=self.baglanti()
            komut=baglan.cursor()
            komut.execute("SELECT * FROM tbl_kayit  ")
            kullanici=komut.fetchone()
            return kullanici
              
    def epostagonder(self):
        try:
            #bağlantı sql den bilgi alır
            kullanici=self.user()
            EPOSTA,ADI,PAROLA=kullanici
            gonderen = "denemepython000@gmail.com"
            parola = "vvzk ulqv qlmf vqia" 
            kime = self.main2.lineEdit.text()
            konu = "Parola Kurtarma ve Gönderi"
            if(kime==EPOSTA):
                mesaj = f" Kullanici:{ADI}\n Parola:{PAROLA}"
                mail = EmailMessage()
                mail["From"]=gonderen
                mail["To"]=kime
                mail["Subject"]=konu
                mail.set_content(mesaj)
               
                icerik = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=icerik) as smtp:
                    smtp.login(gonderen, parola)
                    smtp.sendmail(gonderen, kime, mail.as_string())
                    QMessageBox.information(self,"","Şifreniz başarıyla e-post adresinize gönderildi")   
            else:
                QMessageBox.information(self, "Mail Hatası", "Eposta Yanlış") 
        except Exception as hatakodu:
            QMessageBox.critical(self, "Mail Hatası", "HATA\n"+str(hatakodu))
    
    def listele(self):
        super().__init__()
        self.main = bilgi_Form()
        self.main.setupUi(self)
        self.show()
        tablo = self.main.tableWidget
        self.main.btn2.clicked.connect(self.sil)
        self.main.btn.clicked.connect(self.guncelle)
    
        try:
            kolonlar = ["EPOSTA","ADI"]
            # kolonlardaki değer olarak at
            tablo.setHorizontalHeaderLabels(kolonlar)
            veri = self.baglanti()
            komut = veri.cursor()
            komut.execute("select EPOSTA ,ADI from tbl_kayit")
            rows= komut.fetchall()
            if rows:
                tablo.setRowCount(len(rows)) 
                row_index= 0
                #yazdırmak
                for list in rows:
                    tablo.setItem(row_index, 0, QTableWidgetItem(str(list[0])))
                    tablo.setItem(row_index, 1, QTableWidgetItem(str(list[1])))
                    row_index += 1
            else:
                QMessageBox.warning(self, "Listeleme Boş","Tabloda Veri Bulunamadı")    
        except Exception as hatakodu:
            QMessageBox.warning(self, "Listeleme Hatası",
                        "Bir Hata Oluştu" + str(hatakodu))
    
    def sil(self):
        #satır seçmek
        selected_row = self.main.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "HATA", "Bir satır seçiniz")
            return
        
        #veritaban,san seçilen email
        email = self.main.tableWidget.item(selected_row, 0).text()
        #sql bağlanmak
        baglan=self.baglanti()
        komut=baglan.cursor()
        komut.execute("DELETE FROM tbl_kayit WHERE EPOSTA = ?", ( email,))
        baglan.commit()
        
        self.main.tableWidget.setItem(selected_row,0,QTableWidgetItem(email))
        if komut.rowcount > 0:
            QMessageBox.information(self, "", "Bilginiz silindi")
     
    def guncelle(self):
        #satır seçmek
        selected_row = self.main.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Hata", "Bir satır seçiniz")
            return
        #veritabandan seçilen email
        email = self.main.tableWidget.item(selected_row, 0).text()
        
        yeni_email = self.main.txt_adi.text()
        if not yeni_email:
            QMessageBox.warning(self, "HATA", "Yeni E_mail giriniz")
            return
        baglan=self.baglanti()
        komut=baglan.cursor()
        komut.execute("UPDATE tbl_kayit SET EPOSTA = ? WHERE EPOSTA = ?", (yeni_email, email))
        baglan.commit()
        self.main.tableWidget.setItem(selected_row,0,QTableWidgetItem(yeni_email))
        if komut.rowcount > 0:
            QMessageBox.information(self, "", " Başarıyla güncellendi")


            
        