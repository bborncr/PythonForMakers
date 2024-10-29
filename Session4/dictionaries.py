# dictionaries.py
# dictionaries are key-value pairs AKA hash table AKA lookup table
# note the curly brackets
# dictionaries are structurally similar to JSON
# JSON is a string representation of a dictionary
dogs = {
    "key":"value",
    "Rex":"German Shepard",
    "Fifi":"Poodle",
    "Spot":"Collie"
    }

x = dogs["Fifi"]
print(x)

# lists and dictionaries are frequently used together
students = [
    {
        "name": "Alice",
        "age": 22,
        "major": "Computer Science"
    },
    {
        "name": "Bob",
        "age": 24,
        "major": "Mathematics"
    },
    {
        "name": "Charlie",
        "age": 23,
        "major": "Physics"
    }
]

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")


