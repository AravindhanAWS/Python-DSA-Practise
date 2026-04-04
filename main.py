# Find duplicates using dictionary

list1 =  [1,2,2,4,3,4,4,9,0,23]

freq = {}

count = []

for ch in list1:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
    
    
for key,value in freq.items():
    if value > 1:
        count.append(key)

print(count)


