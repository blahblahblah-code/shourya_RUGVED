str1=input("Enter string:")
prostr=str1.replace(" ","")
l=[]
for i in sorted(prostr):
    if i not in l:
        print(i,prostr.count(i))
        l.append(i)