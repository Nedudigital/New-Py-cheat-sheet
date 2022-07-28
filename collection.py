'''the collections module implements special data types like the : counter, namedtuple, ordereddict, defaultdict, deque'''
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import deque
a = "aaabbbcccc"
my_counter = Counter(a)
print(my_counter.values())
print(my_counter.most_common(2))
'''to check the most common'''
print(my_counter.most_common(2)[0][0])
'''while working on this i faced an error when I ran the program it was because the name of the module and the name of the working file were the same, causing a circular import'''
'''a list with all the different elements'''
print(list(my_counter.elements()))

'''namedtuple, lightweight object type'''
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)

'''OrderedDict a dictionary that remembers order, kinda outdated though'''
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)

'''deque used to remove elements form both ends'''
d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.popleft()
print(d)
d.extend([4, 5, 6])
print(d)
d.rotate(-2)
print(d)




