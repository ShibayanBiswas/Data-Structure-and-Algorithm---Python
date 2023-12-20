################ Interview Questions #############

# Sum and Product

def sum_product(t):
    sum_result = 0
    product_result = 1
 
    for num in t:
        sum_result += num
        product_result *= num
 
    return sum_result, product_result
 
input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24

# Time Complexity : O(n)
# Space Complexity : O(1)




# Elementwise Sum

def tuple_elementwise_sum(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length.")
 
    result = tuple(a + b for a, b in zip(t1, t2))
    return result

# Time Complexity : O(n)
# Space Complexity : O(n)




# Insert at the Beginning

def insert_value_at_beginning(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple

# Time Complexity : O(n)
# Space Complexity : O(n)




# Concatenate

def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)

# Time Complexity : O(n)
# Space Complexity : O(n)




# Diagonal

def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))


# Time Complexity : O(n)
# Space Complexity : O(n)




# Common Elements

def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

# Time Complexity : O(n)
# Space Complexity : O(n)