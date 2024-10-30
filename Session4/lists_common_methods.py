# lists_common_methods.py
# append(), pop(), extend(), insert(), remove(), index(), count(), len(), copy(), sort()
animals = ["lion", "tiger", "cougar", "cheetah", "bobcat"]
animals.extend(["lynx", "puma"])
print(animals)

# insert "panther" into index 2
animals.insert(2, "panther")
print(animals)

# remove first instance of "cougar"
animals.remove("cougar")
print(animals)

# count the number of elements in the list
animals.append("tiger")
x = animals.count("tiger")
print(x)

# return the first index of tiger
x = animals.index("tiger")
print(x)

# return the length of elements in the list
x = len(animals)
print(x)

# this does NOT copy the list...both cats and animals point to the same list
cats = animals

# copy the list -- cats and animals are two independent lists
cats = animals.copy()

print(cats)

cats.sort()
print(cats)
print(animals)

