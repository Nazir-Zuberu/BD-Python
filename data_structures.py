fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple') # Count the # of apples in fruits
fruits.count('tangerine')


fruits.index('banana') # Returns the index of banana
fruits.index('banana', 4)  # Find next banana starting at position 4

fruits.reverse() # returns fruits in a reverse way

fruits.append('grape') # add grape at the end of the list

fruits.sort() # Sort fruits in alphabetical order

fruits.pop() # Remove the last item in fruits


############################################### Using list as Queues ##########################################

# This use the concept of first in first out. It is useful to remove leading items in a list

from collections import deque

queue = deque(["Eric", "John", "Michael"]) # Converting list into a queue
queue.append("Terry")           # Terry arrives. Adding Terry to the queue
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves. Remove the first item



########################################### LIST COMPREHENSION ###################################################

# This is a concise to create a list from another list or iterable object. A list comprehension consist of square
# brackets containing an expression followed by a for clause and then zero or more for or if clauses.
# The expression can be any supported arbitrary expression. It even be another list comprehension. Litterally,
# a list comprehension within list comprehension.

# Traditionally, list of the square of 0-9 is written as follows

squares = []

for i in range(10):
    squares.append(i ** 2)

# print(squares)

# This can also be done using a lambda functions

squares = list(map(lambda x: x **2 , range(10))) # This will apply the lambda function to the range specified

# These can be achieved with list comprehension

squares = [x ** 2 for x in range(10)]


# Two for statement
pairs = [ (a, b) for a in [1, 2, 3] for b in [3, 1, 4]]
print(pairs)


# Adding conditional statemen]

pairs = [ (a, b) for a in [1, 2, 3] for b in [3, 1, 4] if a != b]
print(pairs)

names = ["Naz Beru", "Alex Texa", "Omo Man"]

fnames = [x.split()[0] for x in names]
print(fnames)


########### Nested List Comprehension


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

#
res = [[row[i] for row in matrix] for i in range(4)] 

"""
In this case the expresion is itself a list comprehension.
The inner list compreshension is creating list using the ith element of each row. The ith element of from the row
is determined by the outer iterations.
"""


### Del Statement

# This can be used to remove items from a list using the index of the element. Unlike pop() del does not return
# the deleted element. 


a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0] # Remove -1
del a[2:4] # Remove 333 and 333
[1, 66.25, 1234.5]
del a[:] # Delete all items



 ########################################################## Tuples ###############################################

# Consist of a number of values separated by commas

t = 12345, 54321, 'hello!'
t[0] # return the first item, 12345


# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)

# Tuples are immutable:
t[0] = 88888 # This will return an error

# They can contain mutable objects

v = ([1, 2, 3], [3, 2, 1])

"""
NB: A empty tuple can be created with empty parenthesis. However, a tuple cannot be directly created with one
item. To create a tuple with one element (singleton), you will have to add a comma after the element. 

"""

empty = () # empty tuple
singleton = 'hello',    # <-- note trailing comma
len(empty) # returns 0
len(singleton) # returns 1
error_tuple = (1) # returns an error


########################################################## SET #####################################################

# An unordered collection with no duplicate element. It support mathematical operations like union, intersection,
# difference, and sysmmetric difference. The can be created as set() or {}. When curly brackets are used to create
# a set, they must not be empty. An empty curly bracket will create an empty dictionary



basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
'orange' in basket                 # fast membership testing

'crabgrass' in basket # Returns false since there is no crabgrass in the set


# Demonstrate set operations on unique letters from two words

a = set('abracadabra') # only unique elements will be returned
b = set('alacazam') # only unique elements will be returned
a - b                              # letters in a but not in b
a | b                              # letters in a or b or both. Union of a and b
a & b                              # letters in both a and b
a ^ b                              # letters in a or b but not both


#### SET COMPREHENSION

a = {x for x in 'abracadabra' if x not in 'abc'}
a


############################################ Dictionaries #########################################################


# Contains key value pairs. Values are accessed using assigned keys. 

tel = {'jack': 4098, 'sape': 4139} # Creating a dictionary with the name tel
tel['guido'] = 4127 # Adding item with key 'guido' and value 4127
tel['jack'] # Retrieve the value of 'jack'
del tel['sape'] # delete the value of sape
list(tel) # Return the list of keys in tel in order of insertion
sorted(tel) # Return the ordered list of keys in tel
'guido' in tel # Returns true since guido is in tel
'jack' not in tel # Returns false since jack is in tel


info = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) # Creating a dictionary from a list of tuples


###### Dict Comprehension

squares = {x: x**2 for x in (2, 4, 6)}




dict(sape=4139, guido=4127, jack=4098) # Creating a dictionary from a tuple where the keys are simple strings

names = ['sape', 'guido', 'jack']

values = [4139, 4127, 4098]


repo  = {key:value for key, value in zip(names, values)}
print(repo)


########################################### LOOPING THROUGH SEQUENCES ###########################################

# Looping through a dictionary to return the key value pairs

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key, value in knights.items():
    print(key, value)


# Looping through a list using enumerate. enumerate returns the indexes and the values at those indexes in a
# sequence (list)
    
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# looping multiple sequence can be done using a zip function to pair the elements/items from the sequences
    
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))



basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# basket.sort()
# print(basket)

"""
NB: .sort() only modifies a sequence but returns None as value. After applying the sort method, you must still
work with the original object. sort only modifies it

Sorted on the other hand modifies the sequence and return the modified sequence
"""

### 


import math
import numpy as np
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
sample = [ x for x in raw_data if x.isnumeric()]
print(sample)
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)
# print(filtered_data)


# sample = [ x for x in raw_data if not math.isnan(x)]
# print(sample)

chars = ['ab', 'bc', 'ca']
words = ['abc', 'bca', 'dac', 'dbc', 'cba']

[word for word in words if all(l in chars[i] for i, l in enumerate(word))]