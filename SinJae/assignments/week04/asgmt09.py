n = int(input())

f0 = 0
f1 = 1
fn = 1

for i in range(1, n):
    fn = f0 + f1
    f0 = f1
    f1 = fn

print(fn)