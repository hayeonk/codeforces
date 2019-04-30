def setXY(y, x, delta):
	ok = True
	for i in range(5):
		ny = y + coverType[i][0]
		nx = x + coverType[i][1]
		if ny < 0 or ny >= n or nx < 0 or nx >= n:
			ok = False
		else: 
			board[ny][nx] += delta
			if board[ny][nx] > 1:
				ok = False
	return ok
	
def cover():
	y, x = -1, -1
	for i in range(n):
		for j in range(n):
			if board[i][j] == 0:
				y, x = i, j
				break
		if y != -1:
			break
	
	if y == -1:
		return True
		
	if setXY(y, x, 1):
		if cover():
			return True
	setXY(y, x, -1)
	return False

coverType = [ [0, 0], [1, 0], [1, 1], [1, -1], [2, 0] ]

n = input()
board = [[0] * n for _ in xrange(n)]
for i in xrange(n):
	row = raw_input()
	for j in xrange(n):
		if row[j] == "#":
			board[i][j] = 1
if cover():
	print "YES"
else:
	print "NO"