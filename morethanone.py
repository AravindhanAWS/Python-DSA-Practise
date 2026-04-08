# Find elements appearing more than once

arr1 = [1,2,3,4,4,5,5,6,7,7,7,8]

freq1 = {}

dublicate = []

for ch in arr1:
    freq1[ch] = freq1.get(ch,0) + 1

for key,value in freq1.items():
    if value > 1:
        dublicate.append(key)


print(dublicate)
