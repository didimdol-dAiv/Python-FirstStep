def sol1():
    n = int(input())
    nsum1 = 0
    nsum2 = 1

    for i in range(n):
        nsum1 += nsum2
        nsum2 = nsum1 - nsum2

    print(nsum1)



def sol2():
    n = int(input())

    if n <= 0:
        print(0)
    else:
        fibo = [1, 1]
        for i in range(2, n):
            fibo.append(fibo[i-1] + fibo[i-2])
        print(fibo[-1])



if __name__ == "__main__":
    sol2()
