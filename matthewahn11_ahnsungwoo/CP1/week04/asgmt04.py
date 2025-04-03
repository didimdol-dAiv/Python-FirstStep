    if i % 3 == 0 or i % 5 == 0:
        r += i
N=int(input())
if N == 0:
    result = 0
else:
    result = ""

while N > 0:
    result = str(N%2) + result
    N //= 2
print(result)