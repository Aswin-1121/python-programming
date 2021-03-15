a = [1, 2, 3, 4, 5, 6, 7]
odd = 0
even = 0
for i in a:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
        print("count of even no:s=", even)
        print("count of odd no:s=", odd)
