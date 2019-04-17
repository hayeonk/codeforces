n = input()
A = set(map(int, raw_input().split()))
if len(A) == 1:
	print 0
elif len(A) == 2:
	ans = max(A) - min(A)
	if ans % 2 == 0 and 0 <= min(A) + ans/2:
		ans = ans/2
	print ans
elif len(A) == 3:
	A = list(A)
	A.sort()
	if A[1] - A[0] != A[2] - A[1]:
		print -1
	else:
		print A[1] - A[0]
else:
	print -1