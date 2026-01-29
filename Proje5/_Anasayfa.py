from PyQt6.QtWidgets import*
import sqlite3
from Anasayfa import Ui_Anasayfa
from PyQt6.QtGui import QPixmap
from _kayit import kayit

class Form_Anasayfa(QMainWindow):
   
    def __init__(self):
        super().__init__()
        self.main = Ui_Anasayfa()
        self.main.setupUi(self)
        self.fotoekle()
        self.main.tableWidget.hide()  
        #giriş düğmesi
        self.main2=kayit()
        self.main.Gris.triggered.connect(self.Form_giris)
        self.main3=kayit()
       #kayıt düğmesi
        self.main.kayit.triggered.connect(self.Form_kayit)
        self.main.bs1.clicked.connect(self.urun)
        self.main.bs2.clicked.connect(self.urun)
        self.main.bs3.clicked.connect(self.urun)
        self.main.bs4.clicked.connect(self.urun)
        self.main.bs5.clicked.connect(self.urun)
        self.main.bs5_2.clicked.connect(self.urun)
       #çikiş düğmesi
        self.main.cikis.triggered.connect(self.cikis)    
        
    def baglan(self):
        #urun bilgileri
        with sqlite3.connect("urunler.db")as baglan:
            komut=baglan.cursor()
            komut.execute(f"""  CREATE TABLE IF NOT EXISTS tbl_urun
                        (Adi Text UNIQUE,Fiyat Text)""") 
            return baglan
        
    def urun (self):
        #Gönderen düğmelwri
        sender=self.sender()
        
        baglan=self.baglan()
        komut=baglan.cursor()
        komut.execute("""INSERT OR IGNORE INTO  tbl_urun (Adi,Fiyat) VALUES 
                    ("çanta1", "470.50"),
                    ("çanta1", "470.50"),
                    ("çanta2", "690.95"),
                    ("çanta3", "450.95"),
                    ("Ayakkabı1", "550.20"),
                    ("Ayakkabı2", "920"),
                    ("Ayakkabı3", "720.95")""")
        baglan.commit()
        rows=komut.fetchall()
        #her düğme hangi bilgileri gösterir 
        if sender==self.main.bs1:
            komut.execute(" select Adi, Fiyat From tbl_urun Where Adi='çanta1'And Fiyat='470.50'")     
        elif sender==self.main.bs2:
            komut.execute(" select Adi, Fiyat From tbl_urun Where Adi='çanta2'And Fiyat='690.95'")    
        elif sender==self.main.bs3:
            komut.execute(" select Adi, Fiyat From tbl_urun Where Adi='çanta3'And Fiyat='450.95'")                 
        elif sender==self.main.bs4:
            komut.execute(" select Adi, Fiyat From tbl_urun Where Adi='Ayakkabı1'And Fiyat='550.20'")    
        elif sender==self.main.bs5:
            komut.execute(" select Adi, Fiyat From tbl_urun Where Adi='Ayakkabı2'And Fiyat='920'")
        elif sender==self.main.bs5_2:
            komut.execute(" select Adi, Fiyat From tbl_urun Where Adi='Ayakkabı3'And Fiyat='720.95'")           
        else:
            pass    
        rows = komut.fetchall() 
        #bilgi yazdırma 
        for uye in rows:
                self.main.label_14.setText(str(uye[0]))
                self.main.label_15.setText(uye[1])     
                self.main.tableWidget.show()                               
    
    def fotoekle(self):
       #urun fotolari eklemek
       try:
            
            foto1=QPixmap("foto/1.jpg") 
            self.main.c1.setPixmap(foto1)
            self.main.c1.setScaledContents(True)
            
            foto2=QPixmap("foto/2.jpg") 
            self.main.c2.setPixmap(foto2)
            self.main.c2.setScaledContents(True) 
            
            foto3=QPixmap("foto/3.jpg") 
            self.main.c3.setPixmap(foto3) 
            self.main.c3.setScaledContents(True)
            
            foto4=QPixmap("foto/4.jpg") 
            self.main.a1.setPixmap(foto4) 
            self.main.a1.setScaledContents(True)
            
            foto5=QPixmap("foto/5.jpg") 
            self.main.a2.setPixmap(foto5) 
            self.main.a2.setScaledContents(True)
            
            foto6=QPixmap("foto/6.jpg") 
            self.main.a3.setPixmap(foto6)   
            self.main.a3.setScaledContents(True) 
       except Exception as hata:
           QMessageBox.actions (self,"hata\n"+str(hata))    
        
    def Form_giris(self):
        self.giris = kayit()
        self.giris.show()
        
    def Form_kayit(self):
        self.kayit=kayit()
        self.kayit.show()  
    
    def cikis (self):
        quit()
            

          
            
       
        
                 
        
       

       

        
    
    
    
    
        
        
    
        
    
    
    