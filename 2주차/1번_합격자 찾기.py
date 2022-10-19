for _ in range(int(input())):
	n = int(input())
	v = list(map(int, input().split()))
	avg = sum(v)/n
	count = len([a for a in v if a >= avg])
	print(f"{count}/{n}")
