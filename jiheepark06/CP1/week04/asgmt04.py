N = int(input())
two = ""
while N > 1:
    two = str(N % 2) + two
    N = N // 2
print(str(N) + two)