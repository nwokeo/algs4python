#example: 3-sum
#given n distinct ints, how many triples sum to exactly 0?

#brute force
def threesum(a):
    n = len(a)
    c = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] == 0:
                    c += 1
    return c

print threesum([30, -40, -20, -10, 40, 0, 10, 5])
