for _ in xrange(input()):
	l1, r1, l2, r2 = map(int, raw_input().split())
	if l1 != l2:
		print l1, l2
	else:
		print l1, l2+1