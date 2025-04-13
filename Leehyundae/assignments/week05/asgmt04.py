# 글자 수 세기 함수
def count(a, b):
    return len([i for i in a if i in b])


if __name__ == '__main__':
    a, b = map(str, input().split())
    print(count(a, b))