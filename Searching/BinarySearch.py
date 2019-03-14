

def BinarySearch(liste,aranan):
    liste=sorted(liste)
    
    
    baş=0
    son=len(liste)-1
    
    while(baş<=son):
        ortadaki=(baş+son)//2
        
        if(liste[ortadaki]==aranan):
            return ortadaki,liste
        
        elif(liste[ortadaki]>aranan):
            son=ortadaki-1
        else:
            baş=ortadaki+1
    
    return -1,liste

l=[5,2,3,2,7,4,1,9,6,5]

print(BinarySearch(l,3))
        
    