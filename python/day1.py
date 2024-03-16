t=[]
tri=[]        
def saisirEtremplir(t,):
    global n
    tes=False
    while tes==False:
        n=int(input("n="))
        tes=6<=n<=30
    for J in range(n):
        test=False
        while test==False:
            t[J]=int(input("t[i]"))
            test=1000<=t[i]<=9999
def tablau_trié(t,n,tri):
    cpt=0
    for a in range(n):
        for j in range(n):

            for i in range(str(t[i])):
                if n%int(i)==0:
                    cpt+=1
            if cpt==0:
                t[j]=tri[a]
def affichage(n,t,tri,):
    print(n)
    print(t)
    print(tri)
#pp

saisirEtremplir(t)
tablau_trié(t,n,tri)
affichage(n,t,tri) 

        


