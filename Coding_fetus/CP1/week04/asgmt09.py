#피보나치 수열의 n번째 항 구하기
n = int(input())
fib = [1, 1]
count = 2
for _ in range (n - 2):
    new = fib[count - 2] + fib[count - 1]
    fib.append(new)
    count += 1
print(fib[-1])