#int type을 이진수로 변환하여 출력 (bin()사용 금지)
N = int(input())
k=0
if N % 2 != 0:
    N -=1
elif N % 3 == 0:
    while N != 2:
        N /= 2
        k += 1
print(k)