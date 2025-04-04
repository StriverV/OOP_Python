#---------*args-------------
"""
# If we don't know the number of arguments we'll pass into a function
# *args --> *args creats a tuple of the arguments passed to the function
# We have to add an * before the parameter to use args
# as arguments passed to the function as a tuple
# so order matter
"""

def show(*t):
    print('tuple of the arguments',t)

show(1,2,3,4,5,6,7,4,2,4) #Output: (1, 2, 3, 4, 5, 6, 7, 4, 2, 4)

def add(*t):
    print(sum(t))           # sum is a built in function
add(1,2,3,4,5,6,7,4,2,4)    #Output: 38

def add_args(*t):
    sum_args = 0
    for i in t:
        sum_args += i
    return sum_args
print(add_args(1,2,3,4,5,6))

# We can take normal, default arguments,and args at the same time

def add_mixed(a,b=2,*t):
    sum_args = 0
    for i in t:
        # print(i)    # print args
        sum_args += i
    return sum_args + a + b
print(add_mixed(1,5,3,4,5,6))    # here 1 --> normal , 5 --> default,& 3 to 6 args
