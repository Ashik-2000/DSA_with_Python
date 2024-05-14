set_of_hash = [[], [], [], [], [], [], [], [], [], []]

def hash_function(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char) # ord() returns the unicode integer that represnts the character given in the argument
    return sum_of_char % 10


def add(value):
    index = hash_function(value)
    bucket = set_of_hash[index]
    if value not in bucket:
        bucket.append(value)


def contains(name):
    index = hash_function(name)
    print(f'{name} is in index: {index}')

add('Bob')
add('Lisa')
add('Siri')
add('Pete')
add('Jones')
add('Stuart')

print('Set of hash: ', set_of_hash)

contains('Bob')
contains('Lisa')
contains('Siri')
contains('Pete')
contains('Jones')
contains('Stuart')