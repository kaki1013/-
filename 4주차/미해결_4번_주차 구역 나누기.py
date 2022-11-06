n = int(input())
dp = [0, 0, 1]
mod = 100000007
for i in range(3, n+1):
	temp = (2 * i-1) * dp[-1] + dp[-2]
	dp.append(temp % mod)
print(dp[-1])
