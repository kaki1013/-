def is_finished(N, board):
	for line in board:
		for i in range(N):
			if line[i]:
				return False
	return True

def is_board(N, row, col):
	return (0 <= row < N) and (0 <= col < N)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while not is_finished(N, board):
	temp = [[0]*N for _ in range(N)]
	for row in range(N):
		for col in range(N):
			if board[row][col]:
				temp[row][col] = board[row][col]
				for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
					if is_board(N, row+dx, col+dy) and board[row+dx][col+dy] == 0 and temp[row][col] > 0:
						temp[row][col] -= 1
	board = temp
						
	ans += 1
print(ans)
