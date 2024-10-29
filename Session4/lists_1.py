# lists.py
animals = ["lion", "tiger", "cougar", "cheetah"]

print(animals)
# the default behaviours of a list represent a STACK
# adding to the list with append()
animals.append("bobcat")
print(animals)

# removing from the list with pop()
animals.pop()  # default behaviour removes the last item
print(animals)

# pop() returns the item
animals.append("bobcat")
print(animals)
x = animals.pop()
print(x)
print(animals)

animals.pop(2)
print(animals)

# a list can also be used as a queue by using pop(0)
# pop(0) returns the first item in the list and removes it
# FIFO == First In, First Out
waiting_list = []
waiting_list.append("John")
waiting_list.append("Judy")
waiting_list.append("Jacob")
waiting_list.append("Joan")
waiting_list.append("Jonah")

while waiting_list:
    current_person = waiting_list.pop(0)
    print(f"Currenting attending {current_person}")
    
print("no more jobs")