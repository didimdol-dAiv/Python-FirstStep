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