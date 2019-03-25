n = input()
A = raw_input()
T = ("RGB", "RBG", "GRB", "GBR", "BRG", "BGR")
r, t = min((sum(x != y for x, y in zip(A, t*n)), t) for t in T)
print r
print (t*n)[:n]