# Update/Insert - List

myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33
myList[4] = 55
print(myList)

myList.insert(0,11)
print(myList)

myList.append(55)
print(myList)

newList = [11,12,13,14]
myList.extend(newList)
print(myList)