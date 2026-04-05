# Top K Frequent 

listarr = [1,1,2,2,2,3,3,3,3,3,4,4,5]

freq = {}

k = int(input("Enter the Frequent Number : "))

for num in listarr:
    freq[num] = freq.get(num,0) + 1

sort_items = sorted(freq.items(), key = lambda x: x[1], reverse= True)

result = [key for key,value in sort_items[:k]]

print(result)



    





