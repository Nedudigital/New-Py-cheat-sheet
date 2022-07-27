"""tuples are similar to lists but cannot be changed thus they are immutable ALSO THEY USE (), NOT []"""
mytuple = ("Max", 28, "bOSTON")
print(mytuple)
"""if you have only one entry in your tuple always put a comma behind it so the system will recognize it as a tuple"""
"""to turn an iterable, say a list to a tuple do this"""
mytuple = tuple(["Max", 28, "bOSTON"])
"""you can single out elements by using indexes just like lists"""
"""to count in tuples"""
my_new_tuple = ('a', 'p', 'p', 't', 'k')
print(my_new_tuple.count('p'))
'''slicing with tuples'''
a = (1, 2, 3, 4, 5, 6, 7)
b = a[::-5]
print(b)
'''unpacking'''
new_tuple = "max", 28, 'boston'
name, age, city = new_tuple
print(name)
print(age)
print(city)
'''advanced unpacking'''
i1, *i2, i3 = a
print(i1)
print(i2)
print(i3)
'''when working with large data, tuples seem to be mor efficient we can prove this using the (sys.getsizeof(), "bytes" function or the timeit.timeit(start="",number=1000000 function'''
