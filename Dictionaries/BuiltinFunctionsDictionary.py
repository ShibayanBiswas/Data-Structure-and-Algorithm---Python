my_dict = {
    3:"three",
    5:"five",
    9:"nine",
    2:"two",
    1:"one",
    4:"four"
}

# IN/NOT Operators
print("three" in my_dict.values())
print("ten" not in my_dict.values())

# len()
print(len(my_dict))

# all()
print(all(my_dict))

# any()
print(any(my_dict))

# sorted()
print(sorted(my_dict))