a = int(input())
b = int(input())
print(a+b)

# keyword --> def
def add(n,s):
    print(n+s)
add(a,b)

def op(n,s):
    return n+s,n-s,n*s,n//s    #multi value return
print(op(a,b))

def double_it(n):
    result = n*2
    print(result)
    return result

double_it(5)
double_it(1)

def sum(n1,n2):
    result = n1+n2
    return result

total = sum(1,3)
print('output: ',total)


final = double_it(total)
print('final output: ',final)

