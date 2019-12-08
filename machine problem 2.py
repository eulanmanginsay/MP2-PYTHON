# Problem 2
from math import sqrt 
l=int(input("Value of x1:  "))
m=int(input("Value of y1:  "))
n=int(input("Value of x2:  "))
s=int(input("Value of y2:  "))
t=int(input("Value of x3:  "))
u=int(input("Value of y3:  "))

D=(((n**2)-(l**2))*(u-m)+((s**2)-(m**2))*(u-m)+((l**2)-(t**2))*(s-m)+((m**2)-(u**2))*(s-m)) / ((u-m)*(l-n)-(l-t)*(s-m))
E=(((l**2)-(t**2))*(l-n)+((m**2)-(u**2))*(l-n)+((n**2)-(l**2))*(l-t)+((s**2)-(m**2))*(l-t)) / ((l-n)*(u-m)-(s-m)*(l-t))
F=-(l**2) - (m**2) - (D)*(l) - (E)*(m);

h= D/-2
k= E/-2
r= sqrt((h**2)+(k**2)-(F))

round(h)
round(k)
round(r)

print ("                       ")
print("Vector [D,E,F]: ")
print("[",D,",",E,",",F,"]")
print("Center (h,k): ")
print("(",h,",",k,")")
print("Radius: ")
print("",r,"") 