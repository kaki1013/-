from collections import deque

N, M = map(int, input().split())
money = N
q = deque([])
for _ in range(M):
	cmd, x = input().split()
	x = int(x)
	if cmd == 'deposit':
		money += x
		# 잔액이 늘어났으므로 가능한 거래들은 바로 처리
		while q and q[0] <= money:
			money -= q[0]
			q.popleft()
	elif cmd == 'pay':
		if money >= x:
			money -= x
	elif cmd == 'reservation':	# "대기 목록에 다른 결제가 대기 중이라면.."
		if q or money < x:
			q.append(x)
		else:
			money -= x
print(money)
