# 3 adet farklı şehri rasgele seçen ve kümeye ekleyen python programı yazınız.

import random
sehirler = ["ankara","istanbul","bursa","malatya","mardin","gaziantep"]
rasgelesecim = set()

while (len(rasgelesecim) < 3):
    sehir = random.choice(sehirler) # verilen listede rasgele bir eleman seçer
    rasgelesecim.add(sehir)

print(rasgelesecim)