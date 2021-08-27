# for item in liste:
#     if (koşul):
#         expression

# [expression for item in liste if koşul]



sayilar=[1,5,8,9,15,44]
sonuc=[]
# for sayi in sayilar:
#     if sayi%2==0:
#         sonuc.append(sayi)


sonuc=[i for i in sayilar if i%2==0]                          
sonuc=[sayi if sayi%2==0 else "tek sayı" for sayi in sayilar]   #Farklı kullanışlar, 
print(sonuc)                                                            # else kullanıldığında başa!! DİKKAT, FİLTRELEME YAPIYORUZ


#ÖRNEK
fiyatlar=[1000,2000,4000,0,3000]
vergiliFiyat=[]
           #eski usül
for fiyat in fiyatlar:
    if fiyat>0:
        vergiliFiyat.append(fiyat*1.18)
print(vergiliFiyat)     

     #yeni usül
vergiliFiyat=[fiyat*1.18 if fiyat>0 else "vergi hesaplanmadı" for fiyat in fiyatlar]     
print(vergiliFiyat)



#iç içe list comprehension
sonuc=[]
for x in range(0,3):
    for y in range(0,3):
        sonuc.append((x,y))
print(sonuc)        

sonuc=[(x,y) for x in range(0,3) for y in range(0,3)]
print(sonuc)


