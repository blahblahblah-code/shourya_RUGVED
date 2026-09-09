s=input("Enter string:")
l=list(s)
n=len(l)
for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print("".join(l))