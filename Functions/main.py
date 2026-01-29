## FONKSİYONLARA GİRİŞ
# fonksiyonlar, def kelimesi ile başlar 
# fonksiyon içindeki kod blokları girinti içinde yazılır
# değer döndüren ve döndürmeyen fonksiyonlar vardır
# ana fonksiyonun üzerinde diğer fonksiyonlar tanımlanır ve istenildiği
# yerde çağrılabilirler. 
# fonksiyonların içi hata vermesin diye pass ifadesi ile yazılabilir

def giris():
    yazi = "Fonksiyon Derslerine Başladık"
    return yazi

def fonk2():
    pass

# ana fonksiyon tanımladık
def main():
    # fonksiyon çağırdık
    deger = giris()
    print(deger)
    
main() # ana fonksiyonu çağırdık