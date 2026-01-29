## Dışarıdan alınan veriyi * ile gizler
## pip install pwinput
def ozelparola():
    

    parola = pwinput("Parolanız: ", mask="😊")
    print(parola)

# özel karakter,Büyük-küçük harf, rakam oluşan parola oluşturma fonksiyonu
import string
from random import choice # listeden seçim yap

def parolaOlustur():
    from os import system
    system("cls")
    buyukharf = string.ascii_uppercase
    kucukharf = string.ascii_lowercase
    ozelkarakter = string.punctuation
    rakamlar = string.digits
    for i in range(5):
        print(choice(buyukharf)+choice(kucukharf)+choice(ozelkarakter)+choice(rakamlar),end="")

parolaOlustur()