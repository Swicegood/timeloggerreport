from itertools import product


def factors(n):
    return [i for i in range(1, n // 2 + 1) if not n % i] + [n]

def coprime(a,b):
    for factor in factors(a):
        if factor > 1:
            if b % factor == 0:
                return False
    return True

triples = product(range(100), repeat=3)
count = 0

for triple in triples:
    if triple[0]<triple[1]<triple[2]:
        if triple[0]**2+triple[1]**2 == triple[2]**2:
            if coprime(triple[0],triple[1]):
                if triple[0]+triple[1]+triple[2]<101:
                    print(triple[0],triple[1],triple[2])
                    count = count + 1
                    print (count)
print (count)
