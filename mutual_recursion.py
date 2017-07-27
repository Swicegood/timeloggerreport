def M(n):
    if n == 0:
        return 0
    else:
        return n-F(M(n-1))
def F(n):
    if n == 0:
        return 1
    else:
        return n-M(F(n-1))

for n in range(0,100):
    print(M(n))
    print(F(n))