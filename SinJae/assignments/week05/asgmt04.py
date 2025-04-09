list_ = []

def count(arg1, arg2):
    for i in arg1:
        if arg2 in i:
            list_.append(i)
    return len(list_)