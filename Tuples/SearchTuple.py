#  How to search for an element in Tuple?

newTuple = ('a', 'b', 'c', 'd', 'e')

print('a' in newTuple)

print(newTuple.index('c'))

def searchInTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return 'The element does not exist'

print(searchInTuple(newTuple, 'a'))