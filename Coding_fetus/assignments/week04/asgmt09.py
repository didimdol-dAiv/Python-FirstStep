#피보나치 수열
n = int(input())
a = [1,1]
for i in range(n-2):
    new = a[i]+a[i+1]
    a.append(new)
print(a[-1])