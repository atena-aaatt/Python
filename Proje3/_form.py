from PyQt6.QtWidgets import *
from form import Ui_Form
## ses tanıma dosyasını terminale otomatik doldurması için 
## os modülünü kullandık
from os import system as komut
# ## Modül yükleme
komut("pip install SpeechRecognition")
komut("pip install PyAudio")

## Web Sayfasına Bağlantı Modülleri
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl


## Mail Gönderme Modülleri:
komut("pip install email")
komut("pip install emailmessage")
from email.message import EmailMessage
import ssl, smtplib

## Yazdırma İşlemleri
from PyQt6.QtPrintSupport import QPrinter, QPrintPreviewDialog


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        
        ## Butona Tıklanma Olayları
        self.form.btn_konus.clicked.connect(self.konusma)
        self.form.btn_websitesi.clicked.connect(self.websayfasi)
        self.form.btn_mail.clicked.connect(self.mailgonder)
        self.form.btn_yazdir.clicked.connect(self.yazdir)
        
    def yazdir(self):
        yazici = QPrinter()
        onizleme = QPrintPreviewDialog(yazici)
        onizleme.paintRequested.connect(self.form.txt_mesaj.print)
        onizleme.exec()
    
    def mailgonder(self):
        emailsender = self.form.txt_gonderen.text()
        emailparola = "parola"
        emailreceiver = self.form.txt_alici.text()
        konu = self.form.txt_konu.text()
        mesaj = self.form.txt_mesaj.toPlainText()
        
        em = EmailMessage()
        em["From"] = emailsender
        em["To"] = emailreceiver
        em["Subject"] = konu
        em.set_content(mesaj)
        
        icerik = ssl.create_default_context()
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=icerik) as smtp:
            smtp.login(emailsender, emailparola)
            smtp.sendmail(emailsender, emailreceiver, em.as_string())
        
        
        
        
    
    def websayfasi(self):
        QDesktopServices.openUrl(QUrl("https://enstitu.ibb.istanbul/portal/default.aspx"))
        # QDesktopServices.openUrl(QUrl("mailto://sercan.tirmik@ismek.ist"))
    
    def konusma(self):
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        ## Hata olmasına karşılık hata ayıklama oluşturduk
        try:
            self.form.txt_mesaj.setPlainText(r.recognize_google(audio, language="tr"))
        except sr.UnknownValueError:
            QMessageBox.critical(self,"Ses Hatası","Google Sesi Anlamadı")
        except sr.RequestError as hatakodu:
            QMessageBox.critical(self,"HATA","Bir Hata Oluştu \n" + str(hatakodu))
        
        
        
        
        
        
        