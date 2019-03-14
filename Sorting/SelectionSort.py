import random
import time

def SelectionSort(liste):
    
    for i in range(len(liste)):
        enkucuk=liste[i]
        kucuk_indis=i
        for j in range(i+1,len(liste)):
            if(liste[j]<enkucuk):
                enkucuk=liste[j]
                kucuk_indis=j
            
        gecici=enkucuk
        liste[kucuk_indis]=liste[i]
        liste[i]=gecici
            
                
    return liste
      

liste=[]

for i in range(15000):
    liste.append(random.randint(0,10000))


t1=time.time()
a=SelectionSort(liste)
t2=time.time()
print(t2-t1)



      
liste=[]

for i in range(10000):
    liste.append(random.randint(0,10000))


t1=time.time()
a=SelectionSort(liste)
t2=time.time()

print(t2-t1)
liste=[]

for i in range(5000):
    liste.append(random.randint(0,10000))


t1=time.time()
a=SelectionSort(liste)
t2=time.time()
print(t2-t1)
