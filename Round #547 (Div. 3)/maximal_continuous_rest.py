import sys

rl = lambda: sys.stdin.readline()
n = input()
days = map(int, rl().split())
ret = 0
cur = 0
for i in xrange(2 * n):
	if days[i%n] == 0:
		ret = max(ret, cur)
		cur = 0
	else:
		cur += 1
print ret