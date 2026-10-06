# f=open("k.txt","r")
# content=f.read()
# c=open("p.txt","a")
# c.write(content)

#tell and seek

f=open("k.txt","r+")
content=f.read()
c=open("p.txt","a+")
c.write(content)
