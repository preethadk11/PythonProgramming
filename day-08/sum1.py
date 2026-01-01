'''import os
print(os.getcwd())'''
'''f=open("hello.txt")
for x in f:
    print(x)'''
'''f=open("hello.txt")
line=f.readline()
print(line.strip())
f.close()'''
'''f=open("hello.txt","a+")
f.write("oops this is fucking good")
f.close()
f=open("hello.txt","r")
print(f.read())
f.close()'''
'''import os
if os.path.exists("myfile.txt"):
    print("File exist")
else:
    print("Not exist")'''
'''import os
print(os.getcwd())
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
f=open("myfile.txt","w")
f.write("hello everyone")
f.close()
f=open("myfile.txt","a")
f.write("\nand my name is preetha catherin")
f.close()
f=open("myfile.txt","r")
print(f.read())
f.close()'''
import os
print(os.getcwd())
if os.path.exists("myfile.txt"):
    print("befor delete")
else:
    print("before delete")
with open("myfile.txt","w") as f:
   f.write("Hello everyone")
with open("myfile.txt","r") as f:
    print(f.read())
os.remove("myfile.txt")
if os.path.exists("myfile.txt"):
    print("After delete")
else:
    print("After delete")

