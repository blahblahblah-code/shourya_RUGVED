s=input("Enter alphebetical string:")
l=[]
n=int(input("Enter shift value:"))
for i in s:
    l.append(chr(ord(i)+n))
print("".join(l))