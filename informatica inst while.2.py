temp=0
s=0
p=0
j=0
m=0
i=1
b=0
v=0
while i<=12 :
    i=i+1
    temp= eval(input("dati temperaturile lunilor="))
    
    if temp >=0:
        j=j+1
        s=s+temp
    if temp<0:
        p=p+1
        m=m+temp
b=m/p
v=s/j
print( "temperatura mediie neg. =",b)
print( "temperatura mediie poz. =",v)