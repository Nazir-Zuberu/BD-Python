### Formating with f-string
import sys

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')


## .format()
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
# '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))


# The str()  function is meant to return representation of values which are fairly human-readable 

# The repr() function is meant to generate representation which can be read by the interpreter 

# If an object has no human representation, both repr() and str() returns the same representation

# Numbers and structure have the same representation. String has a different representation for repr() and str()




s = 'Hello, world.'
str(s) # returns 'Hello, world.'
repr(s) # returns "'Hello, world.'"

str(1/7)
'0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
'hello, world\n'
# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"


### Formated String

# This is also known as f-string. 

import math
print(f'The value of pi is approximately {math.pi:.3f}.') # Returns the value of pi correct to 3 decimal places

# Passing an integer after the ':' will cause that field to
# be a minimum number of characters wide. This is useful for 
# making a column line up

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# Values in a formatted string can be converted with
# modifiers before they are formatted. 
    
# !r applies the repr() method 
# !s applies the str() method
# !a applies the ascii() method 
    
animals = 'eels'
print(f'My hovercraft is full of {animals}.') # returns a normal string

print(f'My hovercraft is full of {animals!r}.') # returns the string with eels in inverted commas



##### str.format()

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# Without specifying any values in fields, the 1st item
# in the .format() will be put in the first field and so on
# Indexes of the values in the parenthesis can be passed 
# into the fields; either sequentially or not.

# Values passed to .format() can be keyword argument. In this
# case, the 'keys' will be passed into the provided fields

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

# Similarly, positional and keyword argument can be used too


print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))

# above contains two positional arguments and one keyword argument

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

# Unpacking the dictionary and passing its values as argument

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


# Multiplication tables

for i in range(2,5):
    for j in range(1,13):
        print("{} * {} = {}".format(i,j, i*j))
    print('###########################################')


[ print("{} * {} = {}".format(i,j,i * j), end="\n") for i in range(2,5) for j in range(1,13)] 



for x in range(1, 11):
    print('{:2d} {:3d} {:4d}'.format(x, x*x, x*x*x))





########################################### READING AND WRITING FILES ###############################################

"""
open() returns a file object, and is most commonly used with
two positional arguments and one keyword argument:
open(filename, mode, encoding=None).

Files that are opened using the open() method must be closed 
after use. 

Opening a file with the 'with open()' does not re

"""


f = open('filename', 'w', encoding='utf-8')







