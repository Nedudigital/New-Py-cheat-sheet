'''immutable you cant change string items btw'''
my_string = "I'm a programmer"
print(my_string)
'''triple qusotes are used for double line strings'''
'''assessing strings'''
new_string = "hello world"
char = new_string[-1]
print(char)
'''using slicing to assess substrings'''
new_string = "hello world"
subString = new_string[::2]
print(subString)
'''concatenating 2 or more strings'''
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)
'''we iterate over our string with a for in loop'''
greeting = "Hello"
for x in greeting:
    print(x)
'''you can use if/else too'''
'''using strip() to remove white space'''
'''converting stuff to upper and lower cases'''
mystring = "Hello World"
print(mystring.upper())
print(mystring.lower())
'''you can use startswith() for different conditions'''
mystring = "Hello World"
print(mystring.startswith('H'))
print(mystring.endswith('H'))
'''you can find indexes with find()'''
'''you can count individual characters in strings using count()'''
'''you can replace stuff with replace()'''
'''lists and strings this is how to convert strings to list'''
mystring = "How are you doing"
mylist = mystring.split()
print(mylist)
'''join elements of a list back to a string'''
newstring = ' '.join(mylist)
print(newstring)
'''formatting strings'''
'''new formatiing style'''
var = "Tom"
my_strings = "the variable is {}".format(var)
print(my_strings)
'''regular formatiing style'''
var2 = 3
moi_strings = "the var length is %d" % var2
print(moi_strings)
'''while for floats use %f'''
'''my favorite way is f strings'''
my_string = f"the variable is {var} and {var2}"
print(my_string)





