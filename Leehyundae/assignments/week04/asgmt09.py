def sol1():
    n = int(input())
    nsum1 = 0
    nsum2 = 1

    for i in range(n):
        nsum1 += nsum2
        nsum2 = nsum1 - nsum2

    print(nsum1)


def sol2():
    N = int(input())
    fibo = [1,1]

    for _ in range(N - 2):
        t = len(fibo)
        result = fibo[t-2] + fibo[t-1]

    print(result)


if __name__ == "__main__":
    sol1()