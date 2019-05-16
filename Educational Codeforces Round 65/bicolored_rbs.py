n = input()
s = raw_input().strip()
ans = []
ropen = lopen = 0

for c in s:
	if c == "(":
		if ropen > lopen:
			lopen += 1
			ans.append(1)
		else:
			ropen += 1
			ans.append(0)
	else:
		if ropen > lopen:
			ropen -= 1
			ans.append(0)
		else:
			lopen -= 1
			ans.append(1)
print "".join(map(str, ans))