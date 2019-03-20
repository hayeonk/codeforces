import sys

rl = lambda: sys.stdin.readline().split()
n, m = map(int, rl())
graph = [[] for _ in xrange(n+1)]
for _ in xrange(m):
	u, v = map(int, rl())
	graph[u].append(v)
	graph[v].append(u)

visit = [False] * (n+1)
d = max(len(x) for x in graph)
for i, g in enumerate(graph):
	if len(g) == d:
		v = i
		break

ret = []
visit[v] = True
q = [[u, v] for u in graph[v]]
while q:
	u, v = q.pop(0)
	if visit[u]:
		continue
	visit[u] = True
	ret.append([u, v])
	for v in graph[u]:
		if not visit[v]:
			q.append([v, u])

for u, v in ret:
	print u, v