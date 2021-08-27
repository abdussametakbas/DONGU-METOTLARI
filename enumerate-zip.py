markalar= ["opel", "bmw", "mercedes"]

index=0
for marka in markalar:
    print(f'{index+1}- {markalar[index]}')
    index+=1


#enumerate

obj1= enumerate(markalar)
print(type(obj1))
print(list(obj1))

for index, value in enumerate(markalar,10):      #burda yazılan 10 index i 10 ile başlatır
    print(f'{index}- {value}')                   #   hiçbişey yazmassam 0 ile başlar
    

#zip
liste1= [1,2,3,4,5,]
liste2= ["a","b","c","d","e"]
liste3= [100,200,300,400,500]
print(list(zip(liste1,liste2,liste3)))       #üç listeyi birleştiriyor.

for item in zip(liste1, liste2):           #for döngüsü zaten otomatik listeye çeviriyor.
    print(item)

for key,value in zip(liste1, liste2):
    print(key,value)