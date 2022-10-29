N = int(input())
A = list(map(int, input().split()))
 
count = dict()
for i in range(N):
	s = abs(A[i])
	if s in count:
		count[s][0] = 2
		count[s].append(i)
	else:
		count[s] = [1, i]	# [count, idx1, idx2]
 
ans = 0
for k in count.keys():
	if count[k][0] == 1:
		idx = count[k][1]
		ans += A[idx]
print(ans)


# sol2 : 올바른 쌍끼리의 합은 0임을 이용
N = int(input())
arr = map(int, input().split())
print(sum(arr))
