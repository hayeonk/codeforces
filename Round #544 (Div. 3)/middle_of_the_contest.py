h1, m1 = map(int, raw_input().split(":"))
h2, m2 = map(int, raw_input().split(":"))

mins = ((h2 - h1) * 60 + m2 - m1) / 2
h1 += (mins / 60)
m1 += (mins % 60)
if m1 >= 60:
	m1 -= 60
	h1 += 1

print "%02d:%02d" % (h1, m1)