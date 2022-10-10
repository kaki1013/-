n, k = map(int,input().split())
words = [input() for _ in range(n)]
words.sort()
words.sort(key = lambda x:len(x))
print(words[k-1])
