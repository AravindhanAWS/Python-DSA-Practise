arr1 = [1,2,3,4,5,5,6,6,2,9]
arr2 = [3,3,4,5,4,6,6,7,8,1]

freq1 = {}
freq2 = {}

# Step 1: Frequency count
for num in arr1:
    freq1[num] = freq1.get(num, 0) + 1

for num in arr2:
    freq2[num] = freq2.get(num, 0) + 1

# Step 2: Find common elements with frequency
result = {}

for key in freq1:
    if key in freq2:
        result[key] = min(freq1[key], freq2[key])

print(result)
