n = int(input())
arr = list(map(int, input().split()))
 
ans = 1
for i in range(n):
	ans *= arr[i]
print(ans)
