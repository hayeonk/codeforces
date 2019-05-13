from collections import Counter
import sys
n = input()
A = map(int, raw_input().split())
C = Counter(A)
for i in xrange(n-1, -1, -1):
	S = Counter(C.values())
	if (len(S) == 1 and S.keys()[0] == 1):
		print i + 1
		sys.exit()
	if (len(S) == 1 and S.values()[0] == 1):
		print i + 1
		sys.exit()
		
	if len(S) == 2:
		for x in S:
			if x == 1 and S[x] == 1:
				print i + 1
				sys.exit()
		
		if max(S.keys()) - min(S.keys()) == 1 and S[max(S.keys())] == 1:
			print i + 1
			sys.exit()
		
	C[A[i]] -= 1
	if C[A[i]] == 0:
		del C[A[i]]