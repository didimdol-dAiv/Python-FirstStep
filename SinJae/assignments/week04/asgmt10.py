N = int(input())

pn = 0
npn = 0

for i in range(2,N+1):
    for j in range(2, i):
        if i % j == 0 :
            npn = npn + 1
            break
pn = N - 1 - npn
print(pn)