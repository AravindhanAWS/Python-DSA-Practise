# First Duplicate Element 
 
list1 = [1,2,5,3,4,3,5,5,5]

freq = {}

dublicate = None

for ch in list1:
    freq[ch] = freq.get(ch,0) + 1

print(freq)


for ch in list1:
    for key,values in freq.items():
        if values > 1:
            dublicate = key
            break


print(dublicate)
