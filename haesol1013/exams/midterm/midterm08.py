"""""""""
# [40점] 수치 미분 (권장 풀이 시간: 7분)

## 설명
함수식을 String으로 입력받고, 입력값 x를 받아 함수 결과값 y를 출력해주는 함수 function이 사전 정의되어 있습니다.

함수 정의 내용은 아래와 같고,
def function(func='y=x', x=0):
	return eval(func.split('y=')[1])
	
사용 과정은 아래와 같습니다.
r=function("y=2*x", 10)
print(r) 
-------
20

이 함수를 사용하여 함수의 미분 값을 반환하도록 하고 싶습니다.
그러나 모든 함수에 대한 미분방정식을 자동으로 구할 수 없기 때문에 근사법으로써 '수치미분'을 사용합니다.
함수 이름을 differential로 하고, 함수식과 입력값 x를 인자로 받아 수치미분 값을 반환하도록 하세요.

임의의 값 x에 대한 도함수를 아래와 같이 정의할 수 있고, h를 0에 가까울 정도로 매우 작은 값이라 가정한 후 x와 x+h 사이의 기울기를 구하는 방법을 수치 미분이라고 합니다.

midterm08.png

미분 값을 구하기 위한 오차 h는 1e-8 (=0.00000001)로 하여 계산하세요.

## 입력 설명
첫 번째 인자로 함수식이 String 타입으로 주어집니다.
두 번째 인자로 임의의 값 x가 float 타입으로 주어집니다..

## 출력 설명
임의의 x값을 인자로 받아 함수식의 수치 미분 값을 반환합니다.
(0.00001 미만의 오차는 허용됩니다.)


### 입력 예시 1
"y=2*x"
10
### 출력 예시 1
2.000000165480742

### 입력 예시 2 
"y=x**2"
10
### 출력 예시 2
20.00000165480742

### 입력 예시 3 
"y=log(x)"
2
### 출력 예시 3
0.4999999969612645
"""""""""

from math import *


def function(func='y=x', x=0):
    return eval(func.split('y=')[1])


def function(func='y=x', x=0):
    return eval(func.split('y=')[1])

  
def differential(func,x):
    return (function(func, x + 1e-8) - function(func, x)) / 1e-8


if __name__ == "__main__":
    arg1 = input()[1:-1]
    arg2 = int(input())
    print(differential(arg1, arg2))
