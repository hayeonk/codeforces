from collections import Counter
n = input()
d = map(int, raw_input().split())
D = Counter(d)
x = max(d)
y = 1
for i in D:
	if D[i] == 2 or x % i != 0:
		y = max(y, i)
print x, y