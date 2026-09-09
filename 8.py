s=input("Enter string:")
n=int(input("Enter n:"))
if len(s)%n!=0:
    print("Error: Division is not possible.")
else:
    first=s[0:n]
    is_same=True
    for i in range(0,len(s),n):
        cur=s[i:i+n]
        if cur!=first:
            is_same=False
            break
    if is_same:
        for i in range(0,len(s),n):
            print(s[i:i+n],end=" ")
            print()
    else:
        print("Error: Sequence is not the same.")