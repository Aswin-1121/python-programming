//3. List comprehensions: 
(a) Generate positive list of numbers from a given list of integers 
(b) Square of N numbers 
(c) Form a list of vowels selected from a given word 
(d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values) 



(a)list = [x for x in [1, 2, -3, -2, -5] if x > 0]
print(list)


(b)list=[x**2 for x in range(1,5)]
print(list)


(c)word=input("enter a word")
vowels=['a','e','i','o','u','A','E','I','O','U']
output=[x for x in word if x in vowels]
print(output)


(d)word=input("enter a word")
print("ordinal value is")
for x in word:
    print(word(x))