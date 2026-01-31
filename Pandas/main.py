## exele çevirme işlemi  >  pip install openpyxl

import pandas as pd
veri = pd.read_csv("./olimpiyatlar.csv") 
# dosya.to_html("deneme.html")
print(veri.head(6))
## tablonun türü ve özellikleri, dosya boyutu
# print(veri.info())
## Veri Setinin Sütun Başlığı Bilgisi
print(veri.columns) ## colums değişken tipinde olduğu için parantez yoktur
## veri.rename Veri Seti Sütun Başlıklarını Değiştir (TR olarak değiştir)

veri.rename(
    columns={
        "ID":"ID", "Name":"adi","Sex":"Cinsiyet","Age":"yas",
        "Height":"boy","Weight":"kilo","Team":"takim","NOC":"noc",
        "Games":"oyun","Year":"yil","Season":"sezon","City":"sehir",
        "Sport":"spor","Event":"olay","Medal":"madalya"
    }, inplace=True
)
# inplace=True  : varolan başlık ile yeni başlıkları değiştir
print(veri.head(5))