class SimpleHashSet:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, value):
        sum_of_char = 0
        for char in value:
            sum_of_char += ord(char)

        return sum_of_char % self.size
    
    def add(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            print(f'{value} is in bucket {index}: {bucket}')
        else:
            print(f"The is no value '{value}' in the bucket.")

    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def print_set(self):
        print("The hash set: ")
        for index, bucket in enumerate(self.buckets):
            print(f'Bucket {index}: {bucket}')



hash_set = SimpleHashSet(10)

hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

hash_set.print_set()

hash_set.contains('Peter')
print("Removing 'Peter'")
hash_set.remove('Peter')
hash_set.contains('Peter')
print("'Adele' has hash code:",hash_set.hash_function('Adele'))
hash_set.print_set()


