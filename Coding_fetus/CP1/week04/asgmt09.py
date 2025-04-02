n = int(input())
a = [1,1]
for _ in range (n-2):
    t = len(a)
    N = a[t-2]+a[t-1]
    a.append(N)
print(a[-1])