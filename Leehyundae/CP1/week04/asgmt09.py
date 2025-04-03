n = int(input())
nsum1 = 0
nsum2 = 1

for i in range(n):
    nsum1 += nsum2
    nsum2 = nsum1 - nsum2

print(nsum1)