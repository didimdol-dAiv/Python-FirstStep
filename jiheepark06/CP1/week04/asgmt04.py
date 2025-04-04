N = int(input())
two = ""
for _ in range(10000000000000):
    if N < 2:
        break
    two = str(N % 2) + two
    N = N // 2
two = str(N) + two
print(two)