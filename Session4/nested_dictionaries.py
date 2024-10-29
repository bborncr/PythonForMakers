# nested_dictionaries.py
# List of dictionaries with nested dictionaries
students = [
    {
        "name": "Alice",
        "age": 22,
        "major": "Computer Science",
        "contact": {
            "email": "alice@example.com",
            "phone": "123-456-7890"
        }
    },
    {
        "name": "Bob",
        "age": 24,
        "major": "Mathematics",
        "contact": {
            "email": "bob@example.com",
            "phone": "234-567-8901"
        }
    },
    {
        "name": "Charlie",
        "age": 23,
        "major": "Physics",
        "contact": {
            "email": "charlie@example.com",
            "phone": "345-678-9012"
        }
    }
]

# Accessing the list and nested dictionaries
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")
    print(f"Email: {student['contact']['email']}, Phone: {student['contact']['phone']}")
    
x = students[2]['contact']['phone']
print(x)