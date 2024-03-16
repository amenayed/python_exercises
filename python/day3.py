
def remplir(fam_member):
    for i in range(n):
        fam_member['rank']=input("enter your rank")
        fam_member['age']=input("your age")
        fam_member['name']=input("your name")
        t[i]=fam_member
        
       
def Print(fam_member):
    print("the name of the member is",fam_member['name'])
    print("the age of the member is",fam_member['age'])
    print('the rank of the member is',fam_member['rank'])

#pp
n=int(input("n="))
fam_member=dict(
    name=str(),
    age=int,
    rank=int)
t=[]
#appel
remplir(fam_member)
Print(fam_member)

      
