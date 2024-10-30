# secret_santa_shuffle.py
import random

friends = ["James", "Emma", "Michael", "Olivia", "David"]
random.shuffle(friends)

# final_list = {"James":"Emma", "Emma":"Michael", "Michael":"Olivia"}  etc.
final_list = {}

length = len(friends)

for i in range(length):
    if i < length - 1:
        final_list[friends[i]] = friends[(i+1)]
    else:
        final_list[friends[i]] = friends[0]

print(final_list)