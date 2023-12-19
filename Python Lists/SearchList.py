#  Searching for an element in the List
my_list =  [10,20,30,40,50,60,70,80,90]
# in operator
target = 500
if target in my_list:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")

# Linear search
def linear_search(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return 1
    return -1

print(linear_search(my_list, target))