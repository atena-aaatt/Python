## Sayılar ile ilgili fonksiyon işlemleri:

def toplam(s1 , s2):
    print(s1+s2)
    # return s1+s2

def karesi(sayi):
    print(sayi ** 2) ##   ** sayının üssünü alır

def main():
    ## bir fonksiyon içinde birden fazla fonk. çağrılabilir
    s1 , s2 = 6 , 20
    toplam(s1 , s2)
    karesi(s1)
    # sonuc = toplam(s1 , s2)
    # print(sonuc)

main()