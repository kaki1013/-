from collections import deque
 
N, M, K = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M):
	u, v = map(int, input().split())
	adj[u-1].append(v-1)
	adj[v-1].append(u-1)

dist = [10000] * N
dist[0] = 0
q = deque([(0,0)])
while q:
	curr, ddist = q.popleft()
	for v in adj[curr]:
		if dist[v] == 10000:
			q.append((v, ddist+1))
			dist[v] = ddist+1
print('YES' if dist[N-1] <= K else 'NO')
