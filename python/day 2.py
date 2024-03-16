from random import* 

def sortedStrList(t,n):
    aux=("")
    for i in range(n):
        t[i]=randint(ord('A'),ord('Z'))and randint(ord('a'),ord('z'))
        t[i]=chr(t[i])
    for j in range(n-1):
        if t[j]<t[j-1]:
            aux=t[j]
            t[j]=t[j-1]
            t[j-1]=aux 
    return t,n





t=[""]  
print=(sortedStrList(t,5))
            



        


    
