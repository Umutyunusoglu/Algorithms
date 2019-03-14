def InsertionSort(liste):
    
    for i in range(1,len(liste)):
        
        şimdiki=liste[i]
        
        while(i>0 and liste[i-1]>şimdiki):
            liste[i]=liste[i-1]
            print(liste)
            i=i-1
            liste[i]=şimdiki
            
    
    return liste
        
a=InsertionSort([1,6,4,2,3,7])