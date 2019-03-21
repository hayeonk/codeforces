n, m = map(int, raw_input().split())
A = sorted(map(int, raw_input().split()), reverse = True)
	
def solve(days):
	pages = 0
	for i in xrange(n):
		pages += max(0, A[i] - i/days)
	return pages >= m

res = -1
for days in xrange(1, n+1):
	if solve(days):
		res = days
		break
		
print (res)