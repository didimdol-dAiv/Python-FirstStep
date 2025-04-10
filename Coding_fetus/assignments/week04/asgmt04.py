#4주차 4번 Integer 타입 입력을 2진수로 변환해 출력
n = int(input())

rev_bin = []
if n == 0:
    print('0')

else:
    while n > 0:
        rev_bin.append(n % 2)
        n //= 2
    rev_bin.reverse()
    print(*rev_bin,sep='')