def anag(str1,str2):
    return sorted(str1.lower())==sorted(str2.lower())
str1=input("Enter first string:")
str2=input("Enter second string:")
if anag(str1,str2)==True:
    print("Anagram")
else:
    print("Not Anagram")