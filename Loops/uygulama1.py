# Dışarıdan girilen değerleri sozluk yapısına ekleyen 
# python programı: sozluk.update() kullanımı

ogrenciler = dict()
sayi = int(input("Kaç Öğrenci Eklenecek: ")) # tamsayı girilecek

for a in range(sayi):
    dersler = []
    ogrno = input("Öğrenci No: ")
    adi = input("Öğrenci Adı: ")
    sinifi = input("Sınıfı: ")

    for i in range(3):
        ders = input("Dersi Gir: ")
        dersler.append(ders)

    ogrenciler.update({
        ogrno:{ 
            "adi":adi,
            "sinifi":sinifi,
            "dersler":dersler 
        }
    })
    
for k,v in ogrenciler.items():
    print(k,"\n\t", v)

ogrAra = input("Aranan Öğrenci Nosunu: ")
ogrenciler.get(ogrAra, "Öğrenci Bulunamadı")
ogrenciler.pop(ogrAra)
print(ogrenciler)

