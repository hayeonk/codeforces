n, k = map(int, raw_input().split())
A = map(int, raw_input().split())
S = set()
for i in A:
	S.add((i, i))
	if (i-1, i-1) in S:	
		S.add((i-1, i))
	if (i+1, i+1) in S:
		S.add((i+1, i))
print n + 2*(n-1) - len(S)