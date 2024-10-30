# slicing_lists.py
# sequence[start:stop:step]
# step = includes step
# stop = not including the stop
# step defaults at 1

animals = ["lion", "tiger", "cougar", "cheetah", "bobcat"]

# get the element at the index
x = animals[1]
print(x)

# get the elements from the index up to (but not including 4)
x = animals[1:4]
print(x)

# index of -1 returns the last element
x = animals[-1]
print(x)

# returns all elements up to but not including 4
x = animals[:4]
print(x)

# returns all elements starting at 2
x = animals[2:]
print(x)

# returns every second element
x = animals[::2]
print(x)