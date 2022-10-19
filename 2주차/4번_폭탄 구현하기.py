def is_board(size, x, y):
	return (1 <= x <= size) and (1 <= y <= size)
 
n, k = map(int, input().split())
board = [[0]*n for _ in range(n)]
for _ in range(k):
	a, b = map(int, input().split())
	for dx, dy in [(0,0), (0,1), (0,-1), (1,0), (-1,0)]:
		if is_board(n, a+dx, b+dy):
			board[a+dx-1][b+dy-1] += 1

ans = 0
for i in range(n):
	ans += sum(board[i])
print(ans)
