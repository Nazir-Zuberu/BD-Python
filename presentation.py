

################################### LIST AND LIST COMPREHENSION ##########################

"""
List comprehension is a concise way of creating a list object.
List comprehension can be use to create a new list where each
element is the results of some operations applied to each member
of another sequence or iterable. 

A list comprehension is made up of two main components, an expression
and a for clause. The expression could be from simple to complex expressions.
The expression can also be a list compression. In complex comprehensions,
there could be multiple for and if clauses after the main for clause.


Python List Comprehension Syntax

newList = [ expression(element) for element in oldList if condition ] 


Parameters:

    - expression: Represents the operation you want to execute on every item within the iterable.

    - element: The term “variable” refers to each value taken from the iterable.

    - iterable: specify the sequence of elements you want to iterate through.(e.g., a list, tuple, or string).

    - condition: (Optional) A filter helps decide whether or not an element should be added to the new list.
"""

## Traditionally, we will create a list of squares as follows

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)


## List of squares using list comprehension

squares = [x ** 2 for x in range(10)]
print(squares)

## Compare Performance

import time

for_start = time.time()
squares = []
for x in range(10):
    squares.append(x**2)
for_end = time.time()
for_time = for_end - for_start
print(for_time)

LC_start = time.time()
squares = [x ** 2 for x in range(10)]
LC_end = time.time()
LC_time = LC_end - LC_start
print(LC_time)


## Eg of simple LC

# Using list comprehension to iterate a list
List = [character for character in [1, 2, 3]] 
print(List)


# Using LC to return square of numbers

squares = [i for i in range(11) if i % 2 == 0] 
print(squares)


########## Nested List Comprehensions

"""
Nested List Comprehensions are nothing but a list comprehension
within another list comprehension which is quite similar to nested
for loops. Below is the program which implements nested loop:
"""

## Traditional application

matrix = [] 
  
for i in range(3): 
  
    # Append an empty sublist inside the list 
    matrix.append([]) 
  
    for j in range(5): 
        matrix[i].append(j) 
  
print(matrix) 





##Nested list comprehension 

matrix = [[j for j in range(5)] for i in range(3)] 
  
print(matrix) 


# Display Transpose of 2D- Matrix

twoDMatrix = [[10, 20, 30], 
              [40, 50, 60], 
              [70, 80, 90]] 
  
# Generate transpose 
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix[0]))] 
  
print(trans) 


######################### List Comprehensions and functions ######################
"""
Lambda Expressions are nothing but shorthand representations of
Python functions. Using list comprehensions with lambda creates
an efficient combination. Lets implement the squares example with lambda
function
"""

## lambda application

squares = list(map(lambda x: x**2, [x for x in range(1, 6)]))
print(squares)


## function definition application

# Explicit function 
def digitSum(n): 
    dsum = 0
    for ele in str(n): 
        dsum += int(ele) 
    return dsum 
  
  
# Initializing list 
List = [367, 111, 562, 945, 6726, 873] 
  
# Using the function on odd elements of the list 
newList = [digitSum(i) for i in List if i & 1] 
  
# Displaying new list 
print(newList) 


# inbuilt functions
names = ["Naz Beru", "Alex Texa", "Omo Man"]

fnames = [x.split()[0] for x in names]
print(fnames)


##################################### Python List Comprehension using If-else.############

num = ['one', 'one', 'one', 'two']

lis = [1 if i == 'one'
       else 0 for i in num] 
print(lis) 


############################ Nested IF with List Comprehension ##################

lis = [num for num in range(100)  
       if num % 5 == 0 if num % 10 == 0] 
print(lis)



############################### Creating a list of Tuples from two separate Lists ####################


names = ["Alex", "Maya", "Bray"] 
ages = [25, 30, 35] 
person_tuples = [(name, age) for name, age in zip(names, ages)] 
print(person_tuples)





#### SET COMPREHENSION

a = {x for x in 'abracadabra' if x not in 'abc'}
a


#################################### Dict Comprehension #####################################################

# squares with dict

squares = {x: x**2 for x in (2, 4, 6)}

# 
names = ['sape', 'guido', 'jack']
values = [4139, 4127, 4098]
repo  = {key:value for key, value in zip(names, values)}
print(repo)



