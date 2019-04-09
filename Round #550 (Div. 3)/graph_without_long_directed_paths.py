import sys
from collections import defaultdict
from collections import deque

rl = lambda: sys.stdin.readline().split()
n, m = map(int, rl())

adj = defaultdict(list)
edges = []
for i in xrange(m):
	u, v = map(int, rl())
	adj[u-1].append(v-1)
	adj[v-1].append(u-1)
	edges.append((u-1, v-1))
	
outgoing = [-1] * n
q = deque([[0, 0]])
while q:
	i, out = q.popleft()
	outgoing[i] = out
	for v in adj[i]:
		if outgoing[v] == -1:
			q.append([v, 1 - out])
		elif outgoing[v] == out:
			print "NO"
			sys.exit()
			
ans = ""
for u, v in edges:
	ans += str(outgoing[u])
print "YES"
print ans