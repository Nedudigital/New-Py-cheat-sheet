'''modules used for handling iterators'''
from itertools import product 
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat
import operator
a = [1, 2]
b = [3, 4]
prod = product(a,b)
print(list(prod))

'''permutations, returns all possible ordering of an input'''
a = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))

'''combinations'''
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
'''combinations with replacements'''
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print((list(comb_wr)))
'''accumulate adds stuff in progression'''
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))
'''multiply'''
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))
'''max'''
a = [1, 2, 3, 5, 4]
acc = accumulate(a, func=max)
print(list(acc))
'''groupby'''
'''so basically below we wanted to group the things smaller than 3 in our list, we used the function to define our parameters then we used the groupby function, we put our key as defined in the function and we printed bothy the key(in a boolean form) and the values that were adhered or failed the function '''
def smaller_than_3(x):
    return x < 3
a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))
'''another example using a lambda function'''
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Nedu', 'age': 22}, {'name': 'Claire', 'age': 28}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

'''count, cycle, repeat'''
for i in count(10):
    print(i)
    if i == 15:
        break
'''cycle'''
a = [1, 2, 3]
for i in cycle(a):
    print(i)
    if i == 10:
        break 

'''repeat'''  
a = [1, 2, 3]
for i in repeat(1, 4):
    print(i)
'''test'''


    
