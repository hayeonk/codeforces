n = input()
A = map(int, raw_input().split())
i, j = 0, n-1
ans = []
last = 0
while i <= j:
	if A[i] <= A[j] and A[i] > last:
		last = A[i]
		ans.append("L")
		i += 1
	elif A[j] > last:
		last = A[j]
		ans.append("R")
		j -= 1
	elif A[i] > last:
		last = A[i]
		ans.append("L")
		i += 1
	else:
		break
print len(ans)
print "".join(ans)