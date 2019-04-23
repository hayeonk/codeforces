n, x = map(int, raw_input().split())
A = map(int, raw_input().split())
dpm = [0] * (n+1)
dp = [0] * (n+1)
dpn = [0] * (n+1)
ans = 0

for i in xrange(1, n+1):
	dpm[i] = A[i-1]*x + max(dpm[i-1], dpn[i-1], 0)
	dp[i] = A[i-1] + max(dpm[i-1], dp[i-1], dpn[i-1], 0)
	dpn[i] = A[i-1] + max(dpn[i-1], 0)
	ans = max(ans, dpm[i], dp[i], dpn[i])
print ans