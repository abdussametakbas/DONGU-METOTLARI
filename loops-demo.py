'''
* 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile 
 buldurmaya çalışın. (hak=5) 

* "random" modülü için python random modülü şeklinde arama yapın.

* 100 üzerinden puanlama yapın, her soru 20 puan.

* hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
 üzerinden hesaplansın.
'''
 
import random
sayı = random.randint(1,20)
hak=int(input('kaç tane hak istersiniz? : '))
can=hak
puan= 100

while can>0:
    can-=1

    tahmin= int(input('tahmininizi giriniz: '))
    if tahmin==sayı:
        print(f'tebrikler {hak-can}.defada bildiniz. cevap {sayı}. \n puanınız {puan}')
        break
    elif tahmin>sayı:
        print('düşürün')
        puan-=100/hak
    else:
        print('yükseltin')
        puan-=100/hak
    if can==0:
        print(f'hakkınız bitti. \n puanınız {puan}')            