# 글자 수 세기 함수
def count(a, b):

    c = [i for i in a if i in b]

    return len(c)

if __name__ == "__main__":
    a, b = input().split()
    print(count(a, b))