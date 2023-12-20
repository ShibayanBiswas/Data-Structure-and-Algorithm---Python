# How to access Tuple elements?

newTuple = {'a', 'b', 'c', 'd', 'e'}

# bracket [] operator
print(newTuple[1])

# slice [:] opertor
print(newTuple[1:3])

newTuple[0] = 'f'   # Error because tuples are immutable