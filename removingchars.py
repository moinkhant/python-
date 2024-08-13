f1=open("newtext.txt",'w')
f1.write("hello everyone good morning ")
f1.close()
f2=open("newtext.txt",'r')
print(f2.read())
f2.seek(0)
f3=open("anothertxt.txt",'w')
char=input("enter a char to count its occurences:")
count=0
rc=-1
while(rc):
    rc=f2.read(1)
    if rc==char:
        count+=1
    else:
            f3.write(rc)
f2.close()
f3.close()
print("total count of",char,"is",count)
f4=open("anothertxt.txt",'r')
print(f4.read())
f4.close()
