'''a dictionary is a collection data type that is unordered and mutable, it consists of a collection of keyvalue pairs that map to it's associated value, they are created with {}'''
mydict = {"name": "max", "age": 67, "city": "NEW York"}
print(mydict)
'''
mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)
'''

value = mydict["name"]
print(value)
''''how to add new keyvalue pair'''
mydict["email"] = "nedudigital2000@gmail.com"
print(mydict)
'''how to delete from a dictionary'''
del mydict["name"]
print(mydict)
'''or use pop'''
mydict.pop("age")
print(mydict)
'''to check if a key is present use if statements bro'''
'''or better still use try except statements'''
try:
    print(mydict["name"])
except:
    print("Error, entry not present")
'''for in loops to loop through your dict'''
for value in mydict.values():
    print(value)
'''for copying a dict'''
mydict_cpy = mydict.copy()
print(mydict_cpy)  

'''how to merge two dictionaries'''
mydict2 = dict(name="Mary", age=27, city="Boston")
mydict = {"name": "max", "age": 67, "city": "NEW York"}

mydict.update(mydict2)
print(mydict)
'''use tuple to make dict'''
mytuple = (8, 7)
mydict = {mytuple: 15}

print(mydict)
