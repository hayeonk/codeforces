N, k = map(int, raw_input().split())
A = map(int, raw_input().split())
A = [(n, i) for i, n in enumerate(A)]
ans = [0] * N
turn = 1
while A:
	idx = A.index(max(A))
	l = A[max(0, idx-k):idx+k+1]
	for n, i in l:
		ans[i] = turn
	A = A[:max(0, idx-k)] + A[idx+k+1:]
	if turn == 1:
		turn = 2
	else:
		turn = 1
ans = map(str, ans)
print "".join(ans)