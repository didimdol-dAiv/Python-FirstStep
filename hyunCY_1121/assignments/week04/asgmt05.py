n = int(input())
d = int(input())
result = []

if d == 0 :
    result.append(0)

while d > 0 :
    result.append(d % n)
    d //= n

for i in range(len(result) - 1, -1, -1) :
    print(result[i], end="")
