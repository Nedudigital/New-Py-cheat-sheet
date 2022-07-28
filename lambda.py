from functools import reduce
'''small one line function that works without a name'''
add10 = lambda x: x + 10
print(add10(5))
'''exactly like this:'''
def add10_func(x):
    return x + 10

'''they can also have multiple lines'''
mult = lambda x,y: x+y
print(mult(9,7))

'''lambda and sorted'''
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])

print(points2D)
print(points2D_sorted)

'''map funcs map(func, seq)'''
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))

'''list comprehension'''
c = [x*2 for x in a]
print(c)

'''filter func filter(func, seq) will return all elements for True'''
a = [1, 2, 3, 4, 5]
b = filter(lambda x: x%2==0, a)
print(list(b))

'''with list comprehension(list comp better)'''
c = [x for x in a if x%2==0]
print(c)

'''reduce function reduce(func, seq)'''
a = [1, 2, 3, 4, 5]

product_a = reduce(lambda x,y: x*y, a)
print(product_a)