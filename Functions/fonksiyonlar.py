## Ayrı fonksiyonların bulunduğu dosya
## Ek metotların bulunduğu dosya

##   pip install pyinstaller    
## python dosyasını exe dosyasına çevirir. Bilgisayara bir defa kuruyoruz kullanımı:
## Aynı dizinde KULLANIMI:  pyinstaller main.py  >  VS Code terminale

import os ## işletim sistemi modülü
from time import sleep # zaman modülünde bekleme metodu
from winsound import Beep # frekansa göre ses çalar
 
def cikis():
    Beep(1000, 500)
    print("Program Sonlandı")
    quit()
    os.system("exit") ## Terminali kapat

def menu():
    os.system("cls")
    print(""" DÖRT İŞLEM 
    1- Topla
    2- Çıkar
    3- Üs Alma
    4- Bölüm
    5- Çıkış""")

def topla():
    os.system("cls") # önceki yapılanları sil > ekranı temizle
    sayi1 = int(input("1. Sayı: "))
    sayi2 = int(input("2. Sayı: "))
    print("Sayılar Toplamı:",sayi1+sayi2)
    sleep(1) # 1 saniye bekle

def cikar():
    os.system("cls")
    sayi1 = int(input("1. Sayı: "))
    sayi2 = int(input("2. Sayı: "))
    print("Sayılar Farkı:",sayi1-sayi2)
    sleep(1)

def usalma():
    os.system("cls")
    taban = int(input("Taban Değeri: "))
    us = int(input("Üs Değeri"))
    print(pow(taban,us))
    # print(taban ** us) # yukarıdakinin aynısı
    sleep(1)
    
def bolum():
    os.system("cls")
    bolunen = int(input("Bölünen Sayı: "))
    bolen = int(input("Bölen Sayı: "))
    print("Sayıların Tam Bölümü:", bolunen // bolen)
    sleep(1)