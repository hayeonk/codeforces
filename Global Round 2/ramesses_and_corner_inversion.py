from collections import defaultdict

n, m = map(int, raw_input().split())
A = [map(int, raw_input().split()) for _ in xrange(n)]
B = [map(int, raw_input().split()) for _ in xrange(n)]

def canModify():
	for row1, row2 in zip(A, B):
		if abs(sum(row1) - sum(row2)) % 2 != 0:
			return False
			
	for col1, col2 in zip(zip(*A), zip(*B)):
		if abs(sum(col1) - sum(col2)) % 2 != 0:
			return False
	return True

print "Yes" if canModify() else "No"