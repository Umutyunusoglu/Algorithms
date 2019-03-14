def DoğrusalAra(x,l,birincil=True):
    if birincil:
        for i in range(len(l)):
            if l[i]==x:
                return i
        return None
    
    else:
        r=[]
        for i in range(len(l)):
            if l[i]==x:
                r.append(i)
        return r
    
    
liste=[1,4,6,2,7,4,5,2,4,8,9]

print(DoğrusalAra(2,liste,False))
        
