n = input()
ans = 0
nums = []
while True:
	b = bin(n)[2:]
	if "0" not in b:
		break
	idx = b.index("0")
	nums.append(len(b)-idx)
	n ^= (1 << (len(b)-idx)) - 1
	ans += 1
	
	b = bin(n)[2:]
	if "0" not in b:
		break
	n += 1
	ans += 1
print ans
print " ".join(map(str, nums))