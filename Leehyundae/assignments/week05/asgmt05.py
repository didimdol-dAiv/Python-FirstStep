#Norm2 함수
def norm(a):
    norm1 = 0

    for i in a:
        norm1 += i ** 2

    return round(norm1 ** 0.5, 2)

if __name__ == "__main__":
    a = list(map(float, input().split(" ")))
    print(norm(a))