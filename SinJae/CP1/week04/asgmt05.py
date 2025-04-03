import math


j = int(input())
n = int(input())

result = ""

if j > 1:
    if n:
        k = int(math.log(n) / math.log(j))
    else:
        k = 0
else:
    k = 1

while k >= 0:
    result = result + str(n // j**k)
    n = n - (n // j**k) * (j**k)
    k = k - 1

print(result)


def intresult(N, decimal): #decimal number to base N

    result = 0

    if N > 1:
        if decimal:
            MaxExponent = int(math.log(decimal) / math.log(N)) # N**MaxExponent <= decimal
        else:
            MaxExponent = 0
    else:
        MaxExponent = 1

    while MaxExponent >= 0:
        put_in_number = (decimal // N**MaxExponent)
        result *= 10
        result += put_in_number
        decimal -= (put_in_number * (N**MaxExponent)) #N진수를 10진수로 변환해서 빼줌
        MaxExponent -= 1

    return result


j1 = int(input())
n1 = int(input())

a = intresult(j1, n1)

print(a)

"""

str로 casting 하지 않고 result에 값 저장하는 방법
-result에 10을 곱하고 다음 값을 더해준다
-줄바꿈하지 않고 값을 하나씩 print해준다 -> result에 값을 저장하는 것이 아님
-더 효율적인 다른 방법 고민중...
곱하고 더하는 것보다 같거나 더 적은 time compelxity?
연산 횟수가 한번에서 두번인 방법?
gpt한테 물어보고싶다

result.insert(-1, put_in_number)

"""