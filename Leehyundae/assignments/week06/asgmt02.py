#원소 제거기
def remover(origin, remove):
    return [i for i in origin if str(i) != str(remove)]
