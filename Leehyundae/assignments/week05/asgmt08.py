# softmax 함수
import math

def softmax(*n):

    exp_j = sum(math.exp(j) for j in n )

    return [(math.exp(i) / exp_j) for i in n]


