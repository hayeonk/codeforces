from collections import Counter
n = input()
points = [map(float, raw_input().split()) for _ in xrange(n)]
lines = set()
#for p1, p2 in combinations(points, 2):
for i in xrange(n):
	for j in xrange(i+1, n):
		x1, y1 = points[i]
		x2, y2 = points[j]
		
		if x1 == x2:
			slope = float('inf')
			ysect = x1
		else:
			slope = (y1 - y2) / (x1 - x2)
			ysect = (x1 * y2 - x2 * y1) / (x1 - x2)
			
		lines.add((slope, ysect))

L = [x[0] for x in lines]
C = Counter(L)
total = len(L) * (len(L) - 1) / 2
for x in C:
	total -= C[x] * (C[x] - 1) / 2
print total