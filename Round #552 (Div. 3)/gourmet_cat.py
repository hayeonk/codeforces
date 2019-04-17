A = map(int, raw_input().split())
mult = min(A[0]/3, A[1]/2, A[2]/2)
ans = 7 * mult
A[0] -= 3 * mult
A[1] -= 2 * mult
A[2] -= 2 * mult
day = [0, 1, 2, 0, 2, 1, 0]
def getLongest(A):
	ans = 0
	for i in xrange(7):
		cnt = 0
		tmp = list(A)[::]
		for j in xrange(7):
			if tmp[day[(i+j)%7]] == 0:
				break
			else:
				tmp[day[(i+j)%7]] -= 1
				cnt += 1
		ans = max(ans, cnt)
	return ans
	
ans += getLongest(A)
print ans
	