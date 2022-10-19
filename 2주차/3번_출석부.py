N, k = map(int, input().split())
data = [input().split() for _ in range(N)]
data.sort(key=lambda x:x[1])
data.sort(key=lambda x:x[0])
print(*data[k-1])
