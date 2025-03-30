
def even (a,n):
    flag = True
    for i in range (n):
        if(a[i] % 2 != 0):
            flag = False; 
            break 
    return flag

n = int(input())
a = list(map(int, input().split()))

if(even(a,n)):
    cnt = 0
    while(even(a,n)):
        for i in range (n):
            a[i] //= 2
        cnt += 1
    print(cnt)
    
else:
     print('0')
        
   
