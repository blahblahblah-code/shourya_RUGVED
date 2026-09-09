num=input("Enter credit card number:")
n=len(num)
l=[int(d) for d in num]
for i in range(n-2,-1,-2):
    l[i]*=2
    if l[i]>9:
        l[i]-=9
if sum(l)%10==0:
    print("Valid")
else:
    print("Invalid")