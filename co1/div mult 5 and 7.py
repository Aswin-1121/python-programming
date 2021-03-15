n=[]
for i in range(1000,2001) :
    if (i % 7 == 0) and (i % 5 == 0) :
        n.append(i)
        print("the numbers are:", n)