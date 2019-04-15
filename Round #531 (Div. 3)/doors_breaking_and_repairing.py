n, x, y = map(int, raw_input().split())
A = map(int, raw_input().split())
print n if x > y else (len([k for k in A if k <= x]) + 1) / 2