# break_example.py

animals = ["zebra", "lion", "tiger", "cougar", "tiger"]

for animal in animals:
    if animal == "tiger":
        print("Found the first tiger!")
        break
    else:
        print(animal)
        
print("All done!")