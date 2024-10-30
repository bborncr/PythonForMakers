import random

friends = ["James", "Emma", "Michael", "Olivia", "David"]
hat = friends.copy()

# final_list = {"James":"Emma", "Emma":"Michael", "Michael":"Olivia"}  etc.
final_list = {}

for friend in friends:
    if len(cup) > 0:
        name = random.choice(cup)
        while friend == name:
            print("You can't pick yourself...pick again!")
            name = random.choice(hat)
        hat.remove(name)
        final_list[friend] = name
        
print(final_list)
            