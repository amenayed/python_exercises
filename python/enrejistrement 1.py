from numpy import *
def saisir():
    global n
    n=int(input("donner le nommbre de projet"))
    while not 2<=n<=9:
        n=int(input("donner le nommbre de projet"))



def remplir(t,n): 
    for i in range(n):
        t[i]=dict()
        #date de creation
        t[i]["date_creation"]=dict()
        #jour
        t[i]["date_creation"]["jour"]=int(input("jour:"))
        while not 1<=t[i]["date_creation"]["jour"]<=31:
             t[i]["date_creation"]["jour"]=int(input("jour:")) 
        #mois      
        t[i]["date_creation"]["mois"]=int(input("mois:"))     
        while not 1<=t[i]["date_creation"]["mois"]<=12:
            t[i]["date_creation"]["mois"]=int(input("mois:"))  
        #annee    
        t[i]["date_creation"]["annee"]=int(input("annee:"))        
        while not 1960<=t[i]["date_creation"]["annee"]<=2030:
            t[i]["date_creation"]["annee"]=int(input("annee:"))
        #domaine    
        t[i]["domaine"]=input("domaine=")
        while not 0<=len(t[i]["domaine"])<=15:   
             t[i]["domaine"]=input("domaine=") 
        #nombre de employes
        t[i]["num- emp"]=int(input("nombre de l employe"))
        while not 1<=t[i]["num- emp"]<=100:
            t[i]["num- emp"]=int(input("nombre de l employe"))

        #chef projet
        t[i]["chefp"]=dict()
        #nom
        t[i]["chefp"]["nom"]=input("nom:")
        while not 1<=len(t[i]["chefp"]["nom"])<=15 and "a"<=t[i]["chefp"]["nom"]<="z" and "A"<=t[i]["chefp"]["nom"]<="Z":
            t[i]["chefp"]["nom"]=input("nom:")
        #num
        t[i]["chefp"]["numero"]=int(input("donner votre numero de telephon:"))
        while not 10000000<=t[i]["chefp"]["numero"]<=99999999:
            t[i]["chefp"]["numero"]=int(input("donner votre numero de telephon:"))


def affichage (t,n):
    for i in range(n):
        if t[i]["num- emp"]>22:
            print("domaine de projet a nombre superier a 22:",t[i]["domaine"])
        if t[i]["date_creation"]["annee"]==2022:
            print("les noms des chefes de projet que ont fais un projet dans l anneen 2022 /",t[i]["chefp"]["nom"])








#pp
saisir()  
t=array([dict()]*n)
remplir(t,n)
affichage(t,n)

