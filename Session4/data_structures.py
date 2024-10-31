# data_structures.py
# lists, tuples, dictionaries

# lists ordered mutable sequences of data
# mutable == can be changed IN PLACE
# note the square brackets
animals = ["lion", "tiger", "cougar", "cheetah"]
print(animals)
animals.sort()
print(animals)

# tuples are immutable sequences -- cannot be changed, use less memory, faster
# note the round brackets
animals = ("lion", "tiger", "cougar", "cheetah")
print(animals)

# dictionaries are key-value pairs AKA hash tables
# note the curly brackets
# dictionaries are structurally similar to JSON
# JSON is a string representation of a dictionary
dogs = {
    "key":"value",
    "Rex":"German Shepard",
    "Fifi":"Poodle",
    "Spot":"Collie"
    }

x = dogs["Rex"]
print(x)



