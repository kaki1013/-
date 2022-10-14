n, s = input().split()
ans = 0
for _ in range(int(n)):
	comp = input()
	ans += int(s in comp)
print(ans)
