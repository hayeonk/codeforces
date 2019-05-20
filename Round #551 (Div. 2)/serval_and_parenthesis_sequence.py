n = input()
s = list(raw_input().strip())
if n % 2 == 1:
	print ":("
	exit()
	
maxOpen = n / 2
openCnt = closeCnt = 0
newOpenMax = maxOpen - s.count("(")
newOpen = 0
for i, c in enumerate(s):
	if c == "(":
		openCnt += 1
	elif c == ")":
		closeCnt += 1
	else:
		if newOpen < newOpenMax:
			s[i] = "("
			openCnt += 1
			newOpen += 1
		else:
			s[i] = ")"
			closeCnt += 1
			
	if (openCnt == closeCnt and i != n-1) or openCnt > maxOpen or closeCnt > openCnt:
		print ":("
		exit()
print "".join(s)