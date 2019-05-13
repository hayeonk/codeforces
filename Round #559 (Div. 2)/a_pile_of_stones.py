n = input()
s = raw_input().strip()
cnt = 0
for c in s:
	if c == "+":
		cnt += 1
	else:
		cnt = max(0, cnt - 1)
print cnt