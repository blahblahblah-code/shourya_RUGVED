def hill(num):
    s=str(num)
    n=len(s)
    if n<3:
        return False
    climbing=True
    peak=0
    for i in range(n-1):
        cur=s[i]
        nex=s[i+1]
        if cur==nex:
            return False
        if climbing:
            if cur>nex:
                if i==0:
                    return False
                climbing=False
                peak+=1
        else:
            if cur<nex:
                return False
    return peak==1 and not climbing
a=int(input("Enter number:"))
if hill(a)==True:
    print(a,"is a hill number.")
else:
    print(a,"is not a hill number.")