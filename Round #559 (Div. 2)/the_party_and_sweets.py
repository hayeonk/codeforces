n, m = map(int, raw_input().split())
B = map(int, raw_input().split())
G = map(int, raw_input().split())
if max(B) > min(G):
	print -1
else:
	B.sort()
	row = sum(B)
	maxV = max(B)
	ans = row * m
	G = sorted([x for x in G if x > maxV])
	
	while G:
		b = B.pop()
		for _ in xrange(m-1):
			if G:
				ans += G.pop() - b
	print ans