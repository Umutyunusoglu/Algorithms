import random
import time

def BubbleSort(liste):
    
    for i in range(len(liste)-1):
        
        for k in range(len(liste)-1-i):
            
            if(liste[k]>liste[k+1]):
                    geçici=liste[k]
                    liste[k]=liste[k+1]
                    liste[k+1]=geçici

            
    return liste

liste1=[]
liste2=[]
for i in range(10000):
    liste1.append(random.randint(0,10000))

for i in range(5000):
    liste2.append(random.randint(0,10000))

t1=time.time()
a=BubbleSort(liste1)
print(time.time()-t1)

t2=time.time()
a=BubbleSort(liste2)
print(time.time()-t2)
            