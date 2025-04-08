n = int(input())  
a = list(map(int, input().split()))

freq = {}

for i in range(n):
    if a[i] in freq:
        freq[a[i]] += 1 
    else:
        freq[a[i]] = 1 

        
min_num_of_element = 0
for i,val in freq.items():
    if (val < i):
        min_num_of_element += val
    elif (val > i):
        min_num_of_element += val - i
    
print(min_num_of_element)
