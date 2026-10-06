
#
# 1.file read
# 2.file write
# 3.file append
# 4.file search
# 5.file remove
# 6.exit

def file_read():
    file_name=input("enter filename")
    f=open(file_name,"r")
    content=f.read()
    print(content)

def file_write():
    file_name=input("enter the file name")
    f=open(file_name,"w")
    content1=input("enter the content")
    print(content1)

def file_append():
    file_name=input("enter the filename")
    f=open(file_name,"a")
    content2=input("enter the file content")
    f.write(content2)

def file_search():
    file_name=input("enter the filename")
    f=open(file_name,"r")
    x=f.read()
    content3=input("enter the word")
    if content3 in x:
        print("present")
    else:
        print("not present")

def file_remove():
    import os
    name=input("enter the file name")
    os.remove(name)







while(1):
    print("1.file read")
    print("2.file write")
    print("3.file append")
    print("4.file.seach")
    print("5.file remove")
    print("6.exit")


    ch=int(input("enter your choice"))


    if ch==1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_remove()
    else:
        exit()