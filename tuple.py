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
'''
a=(1,2,3,4,5,6)
print(1 in a)     # returns true if present
'''
#11.Write a Python program to convert a list to a tuple.
'''
a=[1,2,3,4,5]
b=tuple(a)        # tuple is built in function in pyhton 
print(b)
'''

#12.Write a Python program to remove an item from a tuple.
'''
a=(1,2,3,4,5,6)    #cannot remove item frm tuple as tuples are immutable
print(a)            #so we converted tuple into list removed item
b=list(a)           #again converted list into tuple
print(b)
b.remove(2)
print(b)
a=tuple(b)
print(a)

'''
#13.Write a Python program to slice a tuple.
'''
a=(1,2,3,4,5,6,7,8,9)
b=a[1:4]
print(b)
'''

#14.Write a Python program to find the index of an item of a tuple.
'''
a=('a','b','c','d')
b=a.index('d')
print(b)
'''

#15.Write a Python program to find the length of a tuple.
'''
a=(1,2,3,4,5,6,7,8,9,10)
b=len(a)
print(b)
'''

#16. Write a Python program to convert a tuple to a dictionary.
'''
a=[(1,'a'),(2,'b'),(3,'c')]
c=dict(a)
print(c)
'''

#17.Write a Python program to unzip a list of tuples into individual lists.
'''
a=[(1,2,3,4),('pritam','sagar','mayur','abhishek')]
print(list(zip(*a)))
'''
#18.Write a Python program to reverse a tuple.
'''
a=(1,2,3,4,5)
b=list(a)
b.reverse()
a=tuple(b)
print(a)
'''
#19.Write a Python program to convert a list of tuples into a dictionary.
'''
a=[(1,'pritam'),(2,'mayur'),(3,'sagar'),(4,'abhishek')]
b=dict(a)
print(b)
'''

#20.Write a Python program to print a tuple with string formatting.
'''
a=('pritam','kolahpur','DBDA')
print("hello i am %s from %s stream is %s"%a)

'''
'''
a=(100,200,300)
print("this  is tuple",a)
'''

#21.Write a Python program to replace last value of tuples in a list.
'''
a=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1]  +(100,) for t in a])
'''

#22.Write a Python program to remove an empty tuple(s) from a list of tuples.
'''
a=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
b = [c for c in a if c]
print(b)

'''

#23.Write a Python program to sort a tuple by its float element.
'''
a=[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(a, key=lambda x: float(x[1]), reverse=True))
'''

#24.Write Python program to count elements in list until an element is tuple.
'''
num = [10,20,30,(40,50)]
ctr = 0
for n in num:
    if isinstance(n, tuple):
        break
    ctr += 1
print(ctr)

'''


