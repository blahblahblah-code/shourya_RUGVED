n=int(input("Input n:"))
print("Output:")
for i in range(1, n + 1):
    print(" " * (n - i), "*" * i)
for i in range(n, 0, -1):
    print(" " * (n - i), "*" * i)