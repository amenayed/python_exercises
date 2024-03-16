from numpy import*
def saisir():
    global clas
    for i in range(Nc):
        classe[i]=dict()
        classe[i]["niveau"]=int(input("niveau"))
        while not 3<=classe[i]["niveau"]<=4:
            classe[i]["niveau"]=int(input("niveau"))
        classe[i]["section"]=input("section")
        while not classe[i]["section"]in["SI","MA","SC"]:
            classe[i]["section"]=input("section")
        classe[i]["num_de_classe"]=int(input("donner le nombre de classe"))
        while not 1<=classe[i]["num_de_classe"]<=5:
             classe[i]["num_de_classe"]=int(input("donner le nombre de classe"))
        clas=classe[i]     
def affichage_de_class(classe,Nc):
    
    for i in range(Nc):
        
        print(classe[i])
def note_saisir():
    test=False
    while test==False:
        a=int(input("donner un nombre"))
        test=1<=a<=9
       
    for i in range(Nn):
        note[i]=(clas ,"*", a  )
        print(note[i])
#pp
Nc=int(input("donner le nombre de clacce participantes"))
while not 3<=Nc<=10:
    Nc=int(input("donner le nombre de clacce participantes"))
Nn=int(input("donner le taille de tableau de note"))
note=array([dict()]*Nn)
classe=array([dict()]*Nc)
saisir()
affichage_de_class(classe,Nc)
note_saisir()