## Karar yapısı IF - ELIF - ELSE
# 25 > Sıcak
# 15 > Normal
# 0 > Soğuk
## if yapısından sonraki blok tek satırlık ise if yanına yazılabilir
# if yapısında sadece bir if yapısı olur diğer şartlar elif ile bağlanır
# else yapısında yukarıdaki if - elif yapılarından hiçbirisi tutmazsa çalışır

## Notlar Listesine kullanıcının girdiği değerleri çokiyi, iyi şeklinde yazdıran
## python programı yazınız. Kullanıcı sıfır girdiğinde program sonlansın.

# sürekli not isteme işlemini while True ile yapabiliriz.
# 85-100 > COKIYI   75 > IYI  60 > ORTA  0 > ZAYIF   Not sıfır > program sonlansın

notlar = []
while True:
    ogrnot = int(input("Not Girişi: "))
    if (ogrnot == 0):
        break  # ogrnotu sıfır ise döngüyü sonlandırır  
    else:
        if (ogrnot < 0) or (ogrnot > 100):  # yanlış not girilidiğinde
            print("Hatalı not girildi")
        else:
            notlar.append(ogrnot)
            if (ogrnot < 50):   print("ZAYIF")
            elif (ogrnot < 70): print("ORTA")
            elif (ogrnot < 85): print("İYİ")
            else: print("ÇOK İYİ")

print(notlar)
        











sicaklik = int(input("Sıcaklık Gir: "))
if (sicaklik > 25):
    print("Sıcak")
elif (sicaklik > 15):
    print("Normal")
elif (sicaklik > 0):
    print("Soğuk")
else:
    print("Karlı")