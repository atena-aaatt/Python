    
import veritabani

def main():
    while True:
        print("""  Veri Giriş İşlemi
        1- Yönetici
        2- Çalışan
        3- Çıkış """)
        try:
            secenek = int(input("Seçiminiz: "))
            if secenek == 1:
                veritabani.Yonetici().yoneticiekle()
            elif secenek == 2:
                veritabani.Calisan().calisanEkle()
            elif secenek == 3:
                print("Program Sonlanıyor")
                exit()
            else:
                print("1-3 arası seçiniz")
        except Exception as hata_kodu:
            print(hata_kodu)

main()