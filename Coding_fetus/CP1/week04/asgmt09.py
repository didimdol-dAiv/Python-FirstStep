#피보나치 수열의 n번째 항 구하기
n = int(input())
a = [1, 1]
t = 2
for _ in range (n-2):
    N = a[t-2]+a[t-1]
    a.append(N)
    t += 1
print(a[-1])