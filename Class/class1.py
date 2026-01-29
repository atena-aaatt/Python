

class Calisan:
    ## init başlangıç metodudur. (initializing)
    ## Ortak değişken tanımlamaları init içinde yapılır.
    ## self (kendi) : aynı sınıf içindeki farklı metotlarda kullanılan
    ## değişken ve metotların ilişkili olarak görmesini sağlar.
    def __init__(self):
        print(kursadi, "Kursuna Hoş Geldiniz")
        self.yas = input("Yaşınız: ")
    
    def bilgiler(self, sehir):
        adi = input("Adınız: ")
        soyadi = input("Soyadınız: ")
        print(f"{adi}.{soyadi}{self.yas}@ismek.ist")
        print(adi,"yaşadığı şehir:",sehir)

kursadi = input("Kursun Adını Yazınız: ")
sehir = input("Şehir Bilgisi: ")
Calisan().bilgiler(sehir)




