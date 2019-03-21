import sys

rl = lambda: sys.stdin.readline().split()
n = input()
v = map(int, rl())
e = []
g = [[] for _ in xrange(n)]

for _ in xrange(n-1):
	i, j = map(int, rl())
	e.append([i-1, j-1])
	g[i-1].append(j-1)
	g[j-1].append(i-1)

def dfs(i):
	visit[i] = True
	for j in g[i]:
		if not visit[j]:
			dfs(j)

cnt = 0
for i, j in e:
	g[i].remove(j)
	g[j].remove(i)
	visit = [False] * n
	dfs(i)
	g[i].append(j)
	g[j].append(i)
	left = []
	right = []
	for i, b in enumerate(visit):
		if v[i]:
			if b: left.append(v[i])
			else: right.append(v[i])
	
	if len(set(left)) <= 1 and len(set(right)) <= 1:
		cnt += 1
print cnt