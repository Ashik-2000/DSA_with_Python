hash_set=[None, None, None, None, None, None, None, None, None, None]

def hash_function(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)
    
    return sum_of_char % 10

print('Bob has a hash code of: ', hash_function('Bob'))