# softmax 함수
import math

def softmax(a, b, c):
    n = [a, b, c]
    exp_j = 0

    for j in n:
            exp_j += math.exp(j)

    result = [(math.exp(i) / exp_j) for i in n]

    return result



