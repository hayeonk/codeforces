n = input()
nums = map(int, raw_input().split())
nums.sort()
maxCnt = cur = 1
start = 0
for i in xrange(1, n):
	while nums[start] + 5 < nums[i]:
		start += 1
	maxCnt = max(maxCnt, i - start + 1)
	
print maxCnt