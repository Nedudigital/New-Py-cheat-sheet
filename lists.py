'''square brackets for lists'''
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = list()
print(mylist2)
'''a list allows for different data stypes'''
mylist2 = [5, True, "cars"]
print(mylist2)
'''how to call out by referring to the index'''
item = mylist[0]
print(item)
'''negative indexes exist as well'''
item = mylist[-1]
print(item)
'''iterate over your list using for in loops'''
for i in mylist:
    print(i)
''''check if an item is present in list using if and else statements'''
if "lemon" in mylist:
    print("yes")
else:
    print("no")
'''if you want to check how many elements are in your list'''
print(len(mylist))
'''if you want to append items to your list, note append adds stuff to the end of the list'''
mylist.append("pawpaw")
print(mylist)
'''to insert at a specific position by specifying index'''
mylist.insert(1, "blueberry")
print(mylist)
'''pop, if you use the pop command, leave it empyt and equate it to a var you will get the last item on the list, but in turn this removes that item from the list, i.e'''
item = mylist.pop()
print(item)
print(mylist)
'''reverse the list order'''
mylist3 = [4, 2, 3, -1, -5, 10]
item = mylist3.reverse()
print(mylist3)
'''for sorting'''
mylist3.sort()
print(mylist3)
'''sort without changing list'''
newlist = sorted(mylist3)
print(mylist3)
print(newlist)
'''lists and operators'''
newslist = [0] * 5
print(newslist)

new_list = mylist + mylist3
print(new_list)

"""slicing"""
newalist = [1, 2, 3, 4, 5, 6, 7]

a = newalist[::-1]
print(a)
"""copying your list"""
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
list_cpy.append("lemon")
print(list_org)
print(list_cpy)
"""or use the .copy function or use :"""
"""list comprehension"""
a = [1, 2, 3, 4, 5, 6]
b = [i*i for i in a]
print(a)
print(b)