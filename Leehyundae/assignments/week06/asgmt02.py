#원소 제거기
def remover(a, b):
    return [i for i in a if str(i) not in str(b)]
