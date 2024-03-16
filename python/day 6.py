def premier (n):
    
    if n<=1:
        prem=False
    else:
        prem=True
        i=2
        while i<=n//2 and prem==True:
            if n%i==0:
                prem=False
            i+=1
    return prem

print(premier(11))        

