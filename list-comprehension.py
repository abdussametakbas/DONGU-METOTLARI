sayilar=[]

for i in range(0,10):
    sayilar.append(i)
print(sayilar)


# ** list comprehension
sayilar=[i for i in range(0,10)]       # yukarıdaki gibi uzatmak yerine böyle daha kullanışlı
print(sayilar)


isimler=["aHmet","sameT","MeMet"]
sonuc= [i.lower() for i in isimler ]
print(sonuc)





