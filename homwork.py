f=open("swiggy.txt","r")
x=f.readlines()
f=open("zomato.txt","r")
y=f.readlines()

z=x+y
print(z)
d={}
for i in z:
    d[i]=z.count(i)
print(d)