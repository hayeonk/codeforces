n = input()
A = map(int, raw_input().split())
odd = sorted([x for x in A if x%2 == 1], reverse=True)
even = sorted([x for x in A if x%2 == 0], reverse=True)
if abs(len(odd) - len(even)) <= 1:
	print "0"
elif len(odd) < len(even):
	print sum(even[len(odd)+1:])
else:
	print sum(odd[len(even)+1:])