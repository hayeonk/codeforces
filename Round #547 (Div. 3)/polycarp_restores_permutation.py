n = input()
q = map(int, raw_input().split())
ret = [0]
for i in xrange(n-1):
	ret.append(ret[-1] + q[i])

if max(ret) - min(ret) == n-1 and len(set(ret)) == n:
	add = 1 - min(ret)
	ret = map(str, [add + x for x in ret])
	print " ".join(ret)
else:
	print -1