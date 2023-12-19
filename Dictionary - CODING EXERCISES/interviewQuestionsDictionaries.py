################ Interview Questions #############

# Count Word Frequency

def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Time Complexity : O(n)
# Space Complexity : O(n)




# Common Keys

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result

# Time Complexity : O(n+m)
# Space Complexity : O(n+m)




# Key with the Highest Value

def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)

# Time Complexity : O(n)
# Space Complexity : O(1)




# Reverse Key-Value Pairs

def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}

# Time Complexity : O(n)
# Space Complexity : O(n)




# Conditional Filter

def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}

# Time Complexity : O(n)
# Space omplexity : O(n)




# Same Frequency

def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter
    
    return count_elements(list1) == count_elements(list2)

# Time Complexity : O(n1 + n2 + min(m1, m2)), where  n1 and n2 are the lengths of list1 and list2, and m1 and m2 are the numbers of distinct elements in list1 and list2
# Space Complexity : O(m1 + m2)