def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter number:"))
print("The",n,"th fibonacci number is:",fib(n))