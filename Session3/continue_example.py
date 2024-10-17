# continue_example.py
animals = ["zebra", "lion", "tiger", "cougar", "tiger"]

for animal in animals:
    if animal == "tiger":
        print("Nothing to see here...")
        continue
    else:
        print(animal)
        
print("All done!")