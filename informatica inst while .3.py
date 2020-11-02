nr=0
s=0
while (nr%2==1) and (nr%3==0):
    nr= eval(input("dati numere intregi="))
    if nr%2==0:
        s=s+nr
    else: 
        s=s+0   
print ("Suma numerelor pare este =",s)        