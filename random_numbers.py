import random
'''used to generate psuedorandom numbers for various distributions'''
'''random.random will print a random number from 0 - 1'''
a = random.random()
print(a)
'''for specific range'''
a = random.uniform(1, 10)
print(a)
'''to include the upper bound use'''
a = random.randint(1, 10)
'''to never pick the upper or lower bounds use'''
a = random.randrange(1, 10)
print(a)
'''to pick variates'''
a = random.normalvariate(0, 1)
print(a)

'''for sequences'''
mylist = list("ABCDEFGH")
a = random.choice(mylist, 3)
print(a)
'''and if you want a particlular element multiple times use this'''
mylist = list("ABCDEFGH")
a = random.choice(mylist, k=3)
print(a)
'''shuffle'''
mylist = list("ABCDEFGH")
a = random.shuffle(mylist)
print(mylist)
''''''
mylist = list("ABCDEFGH")
a = random.choice(mylist)