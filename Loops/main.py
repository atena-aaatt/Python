## Sözlük > dict() kavramı
## Farklı programlarda json veri tipi olarak kullanılır.

sozluk1 = dict(
            adi="sercan",
            yas=34,
            ilce="küçükçekmece"
        ) 
# boş bir sözlük oluşturur

sozluk2 = {
            "adi":"zeynep",
            "yas":30,
            "ilce":"bahçelievler",
            "yabanciDil":["İngilizce","İspanyolca"]
        } 
# boş bir sözlük oluşturur
print(sozluk1)
print(sozluk2)

print(" ORNEKLER ".center(20,"*"))
print(sozluk1.items()) # dict_items olarak ekranda göster
print(sozluk1.copy())  # küme parantez içinde gösterir
print(sozluk2.keys())  # keys (anahtar) tanımlamasını verir
print(sozluk2.values())# values (değerler) tanımlamasını verir
print(sozluk1.get("yas","Bilgi Yok"))
# arama seçeneği gibi kullanılır. 
# istenen değer yoksa "Bilgi Yok" mesajı verdirilir

print(" DONGU İLE KULLANIM ".center(30,"*"))
sayac = 1
for key, value in sozluk1.items():
    print(sayac, key, value)
    # sayac = sayac + 1
    sayac += 1  # sayacı birer artır, aynı değişkene ekle

print("Döngü Bitti Adım Sayısı:", sayac-1)

print(" KEYS - VALUES İLE KULLANIM ".center(30,"*"))
for key in sozluk1.keys():
    print(key)

for value in sozluk1.values():
    print(value)