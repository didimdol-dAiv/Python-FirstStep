n = int(input())
d = int(input())
bi = ''

if d == 0:
    bi = '0'
else:
    while d > 0:
        bi = str(d % n) + bi
        d = d // n

print(bi)