n = input()
A = map(int, raw_input().split())
def getMax(A):
	n = len(A)
	if sorted(A) == A:
		return n
	return max(getMax(A[:n/2]), getMax(A[n/2:]))
print getMax(A)