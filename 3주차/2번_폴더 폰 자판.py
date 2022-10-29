n = int(input())
s = list(map(int, list(input())))
s.append(10)

char_dict = {1:['!', '1', '.', ',', '?'], 2:['C', '2', 'A', 'B'], 3:['F', '3', 'D', 'E'], 4:['I', '4', 'G', 'H'], 5:['L', '5', 'J', 'K'], 6:['O', '6', 'M', 'N'], 7:['S', '7', 'P', 'Q', 'R'], 8:['V', '8', 'T', 'U'], 9:['Z', '9', 'W', 'X', 'Y']}

if n == 1:
	print(char_dict[s[0]][1])
else:
	separate_idx = [-1]
	for i in range(n):
		if s[i] != s[i+1]:
			separate_idx.append(i)
	ans = []
	for i in range(1, len(separate_idx)):
		value = s[separate_idx[i]]
		count = separate_idx[i] - separate_idx[i-1]
		ans.append(char_dict[value][count%len(char_dict[value])])
	print(''.join(ans))

"""
2
11
.
 
14
44433355556666
HELO
"""
