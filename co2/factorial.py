n = int(input("enter a no:"))
fact = 1
if 0 < n:
   print("factorial does not exist")
elif 0 == n:
    print("factorial of 0 is 0")
else:
    for i in range(1, n+1):
        fact = fact*i
        print("The factorial of", n, "is:", fact)
