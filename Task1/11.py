def cligrade(text):
    wc=len(text.split())
    if wc==0:
        return 0
    lc=sum(c.isalnum() for c in text)
    sc=text.count('.')+text.count('!')+text.count('?')
    L=(lc/wc)*100
    S=(sc/wc)*100  
    CLI= 0.0588*L - 0.296*S - 15.8
    return max(1,CLI)
cli=cligrade(input("Enter text to calculate CLI:"))
print("The text is at Grade readling level",cli)