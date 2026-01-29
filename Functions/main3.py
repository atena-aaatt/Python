## Ana program dosyası (exe dosyası)
## dort işlem menü yapan python programı (fonksiyonlu)

def main():
    import fonksiyonlar as fnk
    ## programın çalıştırılacağı ana fonksiyon
    ## Üç Tırnak print içinde paragraf olarak ekranda gösterir
    while True:
        ## try-except bloğu hata olması olası kod bloklarını kapsayan şekilde yazılır. try: kod blokları ve except altında hata sonucu oluşacak durum belirtilir.
        fnk.menu()
        
        try:
            sec = int(input("Seçiminiz.: "))
            ## if kararları buraya
            if (sec == 5): fnk.cikis() ## 5e basılınca programı bitir
            elif (sec == 1):
                fnk.topla()
            elif (sec == 2): 
                fnk.cikar()
            elif (sec == 3): 
                fnk.usalma()
            elif (sec == 4): 
                fnk.bolum()
            else: 
                ## 1-5 dışında bir şeçim yaparsa hatalı olsun
                print("Hatalı Seçim")
            
        except Exception as hata:
            ## Metinsel bir ifade girilince hata versin
            print("Hatalı Giriş >", hata)


main() # çağırdık