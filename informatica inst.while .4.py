n= int(input("dati numerul intreg="))
s=0
b=1

while b<=n:
    
    s=s+(1*(b-1))
    b=b+1
p=1
b=1

while b<=n:
    p=p*b    
    b=b+1
m=0
a=0
b=1
while b<=n:
    a=a+1
    m=m+b
    b=b+1
print("med.=",m/a)
print("suma=",s)
print("produs=",p)
