# Pitfalls and ways to avoid them

myList = [2,4,3,1,5,7]

'''
myList = myList.sort()
print(myList)
'''

myList.append(10)
print(myList)

myList = myList + [10]
print(myList)

myList.append([10])
print(myList)

'''
myList = [2,4,3,1,5,7]
orig = myList[:]
myList.sort()
print(orig)
print(myList)
'''