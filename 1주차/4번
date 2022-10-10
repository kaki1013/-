n = int(input())
A = list(map(int, input().split()))
 
is_prime = [True] * (n+1)
is_prime[0] = False
is_prime[1] = False
for i in range(n+1):
	if not is_prime[i]:
		continue
	for j in range(2*i, n+1, i):
		is_prime[j] = False
 
ans = 0
for i in range(1, n+1):
	if is_prime[i]:
		ans += A[i-1]
print(ans)
