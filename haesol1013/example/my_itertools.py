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

    functions = (
        product,
        permutations,
        combinations,
        combinations_with_replacement
    )

    for func in functions:
        print("-----------------------")
        print(func.__name__)
        for prod in func(arg, repeat):
            print(prod)
