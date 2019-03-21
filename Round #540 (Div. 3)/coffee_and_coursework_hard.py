n, m = map(int, raw_input().split())
A = sorted(map(int, raw_input().split()), reverse = True)
	
def solve(days):
	pages = 0
	for i in xrange(n):
		pages += max(0, A[i] - i/days)
	return pages >= m

res = -1
lo, hi = 1, n
while lo <= hi:
	mid = (lo + hi) / 2
	if solve(mid):
		res = mid
		hi = mid - 1
	else:
		lo = mid + 1
		
print (res)