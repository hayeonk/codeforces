import sys
n, k = map(int, raw_input().split())

if k * (k-1) < n:
	print "NO"
else:
	print "YES"
	cnt = 0
	for i in xrange(1, k+1):
		for j in xrange(i+1, k+1):
			if cnt + 2 <= n:
				print i, j
				print j, i
				cnt += 2
			elif cnt + 1 <= n:
				print i,j
				cnt += 1
			else:
				sys.exit()