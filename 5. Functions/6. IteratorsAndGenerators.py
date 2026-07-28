"""
LESSON: Iterators and Generators
────────────────────────────────
Both allow you to loop through data ONE ITEM AT A TIME, which saves memory.
# Iterator: An object with a state that remembers where it is.
# Generator: A simpler way to write an Iterator using the 'yield' keyword.
"""
# ITERATOR
nums = [1, 2, 3]

iterator = iter(nums)

print(iterator)

print(next(iterator))         # 1
print(next(iterator))         # 2
print(next(iterator))         # 3

# GENERATOR
def my_gen():
    for i in range(1, 4):
        yield i             # yield pauses and returns value one by one

generator = my_gen()            # Generator is also an iterator

print(generator)
print(next(generator))          # 1
print(next(generator))          # 2
print(next(generator))          # 3

