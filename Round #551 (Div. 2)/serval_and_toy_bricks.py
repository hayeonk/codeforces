n, m, h = map(int, raw_input().split())
front = map(int, raw_input().split())
left = map(int, raw_input().split())
top = [map(int, raw_input().split()) for _ in xrange(n)]

for i in xrange(n):
	for j in xrange(m):
		if top[i][j] == 1:
			top[i][j] = min(front[j], left[i])
for row in top:
	print " ".join(map(str, row))