n1 = int(input())
n2 = int(input())

# a = int(n1) 
# b = int(n2) 
i=n1
flag = False
while i <= n2:
    if i == 4 or i == 7:
        flag = True
        break
    i = i+1
if flag == True:
    print('YES')
else:
    print('NO')