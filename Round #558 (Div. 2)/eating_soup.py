n, m = map(int, raw_input().split())
maxV = n / 2
if m <= 1:
	print 1
elif m == n:
	print 0
elif m <= maxV:
	print m
else:
	print 2 * maxV - m + n%2