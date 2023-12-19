# Dictionary Methods
myDict = {'name':'Edy', 'age':26, 'address':'London', 'education':'master'}

'''
myDict.clear()
print(myDict)
'''
# copy()
dict = myDict.copy()
print(myDict)
print(dict)

# fromkeys()
newDict = {}.fromkeys([1,2,3], 0)   # default is None
print(newDict)

# get()
print(myDict.get('age', 27))
print(myDict.get('city', "Chennai"))

# items()
print(myDict.items())

# keys()
print(myDict.keys())

# popitem()
print(myDict.popitem())
print(myDict)

# setdefault()
print(myDict.setdefault('Number', '1234567890'))
print(myDict)

# pop()
print(myDict.pop('Number', 'not'))

# values()
print(myDict.values())

# update()
newDict = {'a':1, 'b':2, 'c':3}
myDict.update(newDict)
print(myDict)