def palindrome(s, result = 1):
    if len(s) > 1:
        s = list(s)
        first = s.pop(0)
        last = s.pop(-1)

        if first == last:
            result *= 1
        else:
            result *= 0
        return palindrome(s, result)
    else:
        result *= 1
        return result


def palindrome1(s):
    if len(s) <= 1:
        return 1
    else:
        if s[0] == s[-1]:
            s = s[1:-1]
            return palindrome1(s)
        else:
            return 0


if __name__ == "__main__":
    s_ = input()
    print(palindrome1(s_))