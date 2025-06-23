def product(arr: list, r: int=None):
    r = r if r else len(arr)
    def _backtrack(curr, remain):
        if len(curr) == r:
            yield tuple(curr)
        for i, v in enumerate(remain):
            if len(curr) < r:
                yield from _backtrack(curr+[v], remain)
    yield from _backtrack([], arr)


def permutations(arr: list, r: int=None):
    r = r if r else len(arr)
    def _backtrack(curr, remain):
        if len(curr) == r:
            yield tuple(curr)
        for i, v in enumerate(remain):
            if len(curr) < r:
                yield from _backtrack(curr+[v], remain[:i]+remain[i+1:])
    yield from _backtrack([], arr)


def combinations(arr: list, r: int=None):
    r = r if r else len(arr)
    def _backtrack(curr, remain):
        if len(curr) == r:
            yield tuple(curr)
        for i, v in enumerate(remain):
            if len(curr) < r:
                yield from _backtrack(curr+[v], remain[i+1:])
    yield from _backtrack([], arr)


def combinations_with_replacement(arr: list, r: int=None):
    r = r if r else len(arr)
    def _backtrack(curr, remain):
        if len(curr) == r:
            yield tuple(curr)
        for i, v in enumerate(remain):
            if len(curr) < r:
                yield from _backtrack(curr+[v], remain[i:])
    yield from _backtrack([], arr)


if __name__ == "__main__":
    arg = list(map(int, input().split()))
    repeat = int(input())

    for prod in product(arg, repeat):
        print(prod)
    print("-----------------------")

    for perm in permutations(arg, repeat):
        print(perm)
    print("-----------------------")

    for comb in combinations(arg, repeat):
        print(comb)
    print("-----------------------")

    for comb in combinations_with_replacement(arg, repeat):
        print(comb)
    print("-----------------------")


