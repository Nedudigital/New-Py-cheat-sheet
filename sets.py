"""sets are like dictionaries but it does not allow duplicates and no need for key values"""
myset = set("Hello")
print(myset)
'''addind in sets'''
myset = set()

myset.add(1)
myset.add(2)
myset.add(3)
print(myset)
'''clearing and set is like in the other data forms'''
'''iterating over sets using for in loops'''
for x in myset:
    print("yes")

'''Union and intersection of sets, Yes like in math'''
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)
i = odds.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

diff = setB.symmetric_difference(setA)
print(diff)

setA.symmetric_difference_update(setB)
print(setA)
'''super sets and disjoint methods'''
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.issuperset(setB))
'''disjoint'''
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.isdisjoint(setB))

'''COPYING SETS'''
setB = setA.copy()
'''frozen set is the immutable version of a normal set'''
a = frozenset([1, 2, 3, 4])
a.add(2)
print(a)