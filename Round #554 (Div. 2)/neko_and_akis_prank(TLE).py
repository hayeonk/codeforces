n = input()
ans = -1
mod = 10 ** 9 + 7
def count(left, right, cnt):
	global ans
	if cnt:
		ans = (ans+1) % mod
		
	if left < n:
		if right < left:
			if cnt:
				count(left+1, right, 1-cnt)
				count(left, right+1, 1-cnt)
			else:
				count(left+1, right, cnt)
				count(left, right+1, 1-cnt)
		else:
			count(left+1, right, 1-cnt)
	else:
		if right < n:
			count(left, right+1, 1-cnt)
		
count(0, 0, 1)
print ans