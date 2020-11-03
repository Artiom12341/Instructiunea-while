nr=0
s=0
a=1
while a!=0:
    nr= eval(input("dati numere intregi="))
    if((nr%2==1) and (nr%3==0)):
        a=0
    elif nr%2==0:
        s=s+nr
 print ("Suma numerelor pare este =",s)        
