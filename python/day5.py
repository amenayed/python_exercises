
def func1(*var):
    for i in range (len(var)):
        print(var[i])


#func1('amen','dhf',67) 
              
#fonction calculation
def calculation(a,b):
    add=0
    sub=0
    add=a+b
    sub=a-b
    return add,sub

#print(calculation(10,20))
def premier (n):
    comp=0
    for i in range (n):
        if n % i != 0 :
            comp +=1
    if comp==0:
        print(n,"est un nombre premier")
    else:
        print(n," n'est pas un nombre premier")

premier(9)       
     
     



    
