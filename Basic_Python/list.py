#    0  1  2  3  4  5  6  7  8  9   --->Forward index   --> 0 to n-1
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1   --->backward index  --> -n to -1

# print(list)  #output--> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# -------------Slicing---------------- 
# list[start: end: step]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# If we don't define the start or end index, 
# it will by default take the start (as 0 th index),and end (as n-1) indices of the list.

# print(a[:])      #or print(a[::]), output-->[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a[::-1])   # reverse --> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(a[0::]) 
# print(a[::2])    #[1, 3, 5, 7, 9]



# ------------list methods -----------------
l = [10, 20, 30, 40, 50]
print(l)      #[10, 20, 30, 40, 50]

# l.append(val)
l.append(100)
print(l)      # [10, 20, 30, 40, 50, 100]

# l.insert(index,val)
l.insert(2,5000)
print(l)      # [10, 20, 5000, 30, 40, 50, 100]


# l.remove(val)
l.remove(5000)
print(l)      # [10, 20, 30, 40, 50, 100]


# pop(index)
l.pop(3)  
print(l)      # [10, 20, 30, 50, 100]
# l.pop()
l.pop() 
print(l)      # [10, 20, 30, 50]

# index(val)    ---> it will return the index of the value 
l.index(10)
print(l.index(10))   # 0



#-------------- Using Lists as Stacks(LIFO)-----------
ls = [10, 20, 30, 40, 50]
# To add an item to the top of the stack, use append()
ls.append(100)
print(ls)      # [10, 20, 30, 40, 50, 100]

# To remove an item from the top of the stack, use pop()
ls.pop() 
print(ls)      # [10, 20, 30, 50]


# ------------Using Lists as Queues(FIFO)----------
from collections import deque
lq = deque([10, 20, 30, 40, 50])

lq.append(33)           
print(lq)     # deque([10, 20, 30, 40, 50, 33])

lq.popleft()
print(lq)     # deque([20, 30, 40, 50, 33])

#  -----generate a new list  by list comprehension ------

lc = []
for i in range(5):
    lc.append(i*i)

print(lc)   #[0, 1, 4, 9, 16]

#or
# lambda function
# lc1 = list(map(lambda i : i*i, range(5)))
# print(lc1)

# # or 
# lc2 = [i*i for i in range(5)]  # most Pythonic approach
# print(lc2)


a = [45, 87, 96, 65, 43, 90, 85, 14, 26, 61, 70]
odds = []
for i in a:
    if i % 2 == 1 and i % 5 == 0:
        odds.append(i)
print(odds)   # [45, 65, 85]

# or
odd1 = [i for i in a if i % 2 == 1 if i % 5 == 0]



# nested loop
n = ['n', 'j', 'n']
a = [20, 21, 22]

comb = []
for i in n:
    for j in a:
        comb.append([i, j])
        
print(comb)

# or
comb1 = [[i, j] for i in n for j in a]
print(comb1)
# [['n', 20], ['n', 21], ['n', 22], ['j', 20], ['j', 21], ['j', 22], ['n', 20], ['n', 21], ['n', 22]]
