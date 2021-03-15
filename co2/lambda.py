#square
square=lambda a:a*a
n=int(input("enter the side of square :"))
print(square(n))

#rectangle
rectangle=lambda l,b:l*b
print("enter length and breadth of rectangle :")
l=int(input())
b=int(input())
print(rectangle(l,b))

#triangle
triangle=lambda b,h:(b*h)/2
print("enter breadth and height of triangle :")
b=int(input())
h=int(input())
print(triangle(b,h))