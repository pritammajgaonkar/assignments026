#1.Write a Python program to create a tuple.
'''
a=(1,2,3,4,5,6,6,5,4,3,2,1)
print(a)
'''
#2.Write a Python program to create a tuple with different data types.
'''
b=("True",0.12,12,'hi')
print(b)
'''

#3.Write a Python program to create a tuple with numbers and print one item.
'''
a=(1,2,3,4,5)
print(a[2])
'''
#4.Write a Python program to unpack a tuple in several variables.
'''
a=('Pritam','kolhapur','ENTC')
(name,city,stream)=a
print(name,city,stream)
'''
#5.Write a Python program to add an item in a tuple.
'''
a=(1,2,3,4,5)
b=a[2]+a[3]
print(b4)
'''
#6.Write a Python program to convert a tuple to a string.
'''
a=('a','b','c','d','e')
b="".join(a)   # join is used to convert tuple to string
print(b)
'''
#7. Write a Python program to get the 4th element and
#4th element from last of a tuple.
'''
a=(0,1,2,3,4,5,6,7,8,9)
print(a[4])  #gives 4th element in tuple
print(a[-4]) #gives 4 th element from last
'''
#8.Write a Python program to create the colon of a tuple.
'''
a=(1,2,[],4)
a[2].append(3)
print(a)
'''
#9.Write a Python program to find the repeated items of a tuple.
'''
a=(1,2,3,4,5,6,5,4,3,5)
b=a.count(5)
print(b)
'''

#10.Write a Python program to check whether an element exists within a tuple.

a=(1,2,3,4,5,6)
print(1 in a)     # returns true if present
