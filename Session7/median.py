# median.py
raw_data = [1,2,3,5,7,8,400,7,6,5,4,3,6,5,2,1]
sorted_data = raw_data.copy()
sorted_data.sort()
median = sorted_data[len(sorted_data)//2]
print(median)
print(raw_data)
raw_data.append(3)
raw_data.pop(0)
print(raw_data)