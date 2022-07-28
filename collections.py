'''the collections module implements special data types like the : counter, namedtuple, ordereddict, defaultdict, deque'''
from collections import Counter
a = "aaabbbcccc"
my_counter = Counter(a)
print(my_counter.items())
