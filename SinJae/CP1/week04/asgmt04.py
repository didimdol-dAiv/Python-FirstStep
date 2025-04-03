import math


n = int(input())
result = ""

if n != 0:
    max_exponent = int(math.log2(n))
else:
    max_exponent = 0

while max_exponent >= 0:
    if n >= 2**max_exponent:
        result += "1"
        n = n - 2**max_exponent
    else:
        result += "0"
    max_exponent -= 1

print(result)
