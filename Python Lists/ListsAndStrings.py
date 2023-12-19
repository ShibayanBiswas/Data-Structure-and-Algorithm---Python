# Strings and Lists

a = 'spam spam spam'
b = a.split()
print(b)

a1 = 'spam-spam1-spam2'
delimeter = '-'
b=a.split(delimeter)
print(b)
print(delimeter.join(b))