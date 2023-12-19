prev_list = [-1,10,-20,2,-90,60,45,20]
new_list = [number+number for number in prev_list if number < 0]
print(new_list)


sentence = 'My name is Shibayan'
def is_consonant(letter):
    vowvels = 'aeiou'
    return letter.isaplpha() and letter.lower() not in vowvels
print(is_consonant('t'))


consonants = [i for i in sentence if is_consonant(i)]
print(consonants)


prev_list = [-1,10,-20,2,-90,60,45,20]
new_list = [number if number > 0 else 'negetive number' for number in prev_list]
print(new_list)


def get_number(number):
    if number > 0:
        return number
    else:
        return 'negetive number'

prev_list = [-1,10,-20,2,-90,60,45,20]
new_list = [get_number(number) for number in prev_list]
print(new_list)