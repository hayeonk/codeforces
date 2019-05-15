import sys
rl = lambda: sys.stdin.readline().split()

n, x, y = map(int, rl())
A = raw_input().strip()
r = "0" * (x-y-1) + "1" + "0" * y
cnt = 0
for c1, c2 in zip(r, A[-x:]):
	if c1 != c2:
		cnt += 1
print cnt