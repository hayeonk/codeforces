import math
n, t = map(int, raw_input().split())
A = [map(int, raw_input().split()) for _ in xrange(n)]
ans = None
cur = float('inf')
for i in xrange(n):
	s, d = A[i]
	if s >= t:
		if s < cur:
			cur = s
			ans = i + 1
	else:
		time = s + math.ceil(float(t-s)/d) * d
		if time < cur:
			cur = time
			ans = i + 1
print ans