t = int(input())
for i in range(t):
# while t > 0:
	n = int(input())
	a = list(map(int, input().split()))
	minR = 10**9         # like  minR = INT_MAX in cpp
	for i in range(n):    # 0 to n-1
		for j in range(i + 1, n):     # i+1 to n-1
			result = a[i] + a[j] + j - i
			minR = min(result, minR)
      
	print(minR)  
	# t -= 1  
	    

	    
	

