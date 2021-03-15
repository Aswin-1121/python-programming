def fibonacci(m):
    if n<0:
        print("cannot find fibonacci")
    else:
       a=0
       b=1
       print(a)
       print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
n=int(input("enter a number"))
fibonacci(n)