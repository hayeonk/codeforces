n = input()
A = map(int, raw_input().split())
i, j = 0, n-1
ans = []
last = 0
while i <= j:
	if i == j or A[i] != A[j]:
		if A[i] < A[j] and A[i] > last:
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
	else:
		r = j
		right = []
		tmp = last
		while i < r and A[r] > last:
			last = A[r]
			right.append("R")
			r -= 1
		l = i
		left = []
		last = tmp
		while l < j and A[l] > last:
			last = A[l]
			left.append("L")
			l += 1
		if len(left) > len(right):
			ans += left
		else:
			ans += right
		break
print len(ans)
print "".join(ans)