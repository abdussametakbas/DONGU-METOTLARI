#  1 - çarpım tablosu hazırlayınız
for x in range(1,11):
    for y in range(1,11):
        çarpım= x*y
        print(f'{x}*{y} = {çarpım}')




#  2 - girilen her bir sayının asal olup olmadığını kontrol edin.
sayi = int(input('Bir sayı giriniz: '))
AsalMi=True

if sayi==2:
    AsalMi=False

i=2
for i in range(i,sayi):
    if sayi%i==0:
        AsalMi=False
        break    

if AsalMi:
    print(f'{sayi} asaldır')
else:
    print(f'{sayi} asal değildir.')


