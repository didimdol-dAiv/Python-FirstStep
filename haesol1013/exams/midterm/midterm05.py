"""""""""
# [50점] Sliding Window (권장 풀이 시간: 10분)

## 설명
목표 Vector(또는 Tensor) 보다 작은 Vector(또는 Tensor)가 목표 Vector를 순회하며 지역적으로 연산하는 방법을 Sliding Window라고 합니다.
아래 그림은 길이가 7인 Vector를 길이가 3인 Window Vector가 순회하며 Summation 연산을 하는 Sliding Window 알고리즘의 과정입니다.

midterm05.png

함수의 이름을 sliding_window로 하고, 목표 Vector와 window의 길이가 인자로 주어질 때 지역적으로 Summation 연산 후 발생하는 결과 Vector를 반환하는 함수를 정의하세요.

허용 라이브러리 : numpy , math

## 입력 설명
첫 번째 인자로 목표 Vector가 Integer타입 1차원 Numpy array로 주어집니다.
두 번째 인자로 Window의 길이가 Integer 타입으로 주어집니다. (단, 길이는 1이상이고 목표 Vector보다는 작으며 항상 홀수입니다.)

## 출력 설명
Sliding window의 결과로 발생한 Vector를 Numpy array 또는 기타 Iterable 타입(List, Tuple 등)으로 반환해야 합니다.


### 입력 예시 1 
[1,2,3,4,5]
3
### 출력 예시 1
[6,9,12]

### 입력 예시 2 
[1,2,3,4,5,6,7,8,9]
5
### 출력 예시 2
[15,20,25,30,35]
"""""""""

def sliding_window(arr: list[int], size: int) -> list[int]:
    return [sum(arr[i:i+size]) for i in range(len(arr) - size + 1)]


if __name__ == "__main__":
    arg1 = list(map(int, input()[1:-1].split(",")))
    arg2 = int(input())
    print(sliding_window(arg1, arg2))
