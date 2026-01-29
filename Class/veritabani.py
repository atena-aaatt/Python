
import sqlite3
from random import randint as rnd # idno için rasgele tamsayı üret

class Calisan:
    def bilgi(self):
        ## Yonetici sınıfında da ad,soyad,maas bilgileri kullanabilmek için self kullandık
        self.adi = input("Adınız: ")
        self.soyadi = input("Soyadınız: ")
        self.maas = int(input("Maaş: "))
    
    # Aynı sınıf içindeki metotlarda öncelik ilişkisi self ile çağrıldığı için yoktur.
    def calisanEkle(self):
        idno = rnd(100,500) # veritabanını yormamak için en başta yaptık.
        self.bilgi() ## kişinin adsoyad,maaş gibi bilgilerine eriş
        baglanti = self.calisan_baglantisi() # tablonun olup olmadığını kontrol ettik
        komut = baglanti.cursor()
        ## kayıt ekleme sorgusu
        komut.execute(f""" insert into tbl_calisan values
                      ({idno},"{self.adi}","{self.soyadi}",{self.maas})  """)
        baglanti.commit() ## DB değiştiği için onayladık
        

    def calisan_baglantisi(self):
        with sqlite3.connect("calisanlar.db") as baglanti:
            komut = baglanti.cursor()
            ## Çalışan Tablosunu Oluşturuyoruz
            komut.execute(""" create table if not exists tbl_calisan 
                         (idno INT, adi TEXT, soyadi TEXT, maas INT)  """)
            return baglanti
    

# super() > kalıtım aldığı metodun init metoduna gider
## init yoksa hangi metot tanımlıysa ona işlem yapar.
class Yonetici(Calisan):
    def bilgi(self):
        super().bilgi()
        self.unvan = input("Unvan Bilgisi: ")
        self.uzmanlik = input("Uzmanlık Alanı: ")
        # print(" Yönetici Bilgileri ".center(30,"-"))
        # print(f""" 
        # Adı Soyadı: {self.adi} {self.soyadi}
        # Maaş......: {self.maas}
        # Unvan.....: {unvan}
        # Uzmanlık..: {uzmanlik} """)  
    
    def yoneticiekle(self):
        idno = rnd(100,500)
        self.bilgi()
        baglanti = self.yonetici_baglantisi()
        komut = baglanti.cursor()
        komut.execute(f""" insert into tbl_yonetici values
                      ({idno},"{self.adi}","{self.soyadi}",{self.maas},
                       "{self.unvan}", "{self.uzmanlik}")  """)
        baglanti.commit() ## DB değiştiği için onayladık
        
    
    def yonetici_baglantisi(self):
        with sqlite3.connect("calisanlar.db") as baglanti:
            komut = baglanti.cursor()
            ## Yonetici Tablosunu Oluşturuyoruz
            komut.execute(""" create table if not exists tbl_yonetici 
                        (idno INT, adi TEXT, soyadi TEXT, maas INT,
                        unvan TEXT, uzmanlik TEXT)  """)
            return baglanti
