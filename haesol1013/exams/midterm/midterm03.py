"""""""""
# [60점] 취객의 삼각수 패턴 (권장 풀이 시간: 20분)

## 설명
수학을 사랑하는 안고홀 씨는 궁동에서 과하게 음주를 해버렸습니다.
안고홀 씨는 만취했을때 특유의 걸음걸이 패턴을 가지고 있습니다.

삼각수 규칙에 따라 좌우로 왔다갔다하며 걷는 패턴을 가지고 있는 것입니다.
예를 들어, 오른쪽으로 한 걸음 움직였다면 왼쪽으로 두 걸음, 다시 오른쪽으로 세 걸음으로 움직이는 패턴입니다.
따라서 6번째 걸음 이 후 안고홀 씨의 위치는 1-2+3의 패턴을 따라 오른쪽 두 걸음 위치에 있을 것입니다.

그러나 안고홀 씨는 제자리에서 좌우로 움직이는게 아니라 앞으로 전진하기 때문에 위치가 계속해서 변합니다.
아래 그림과 같이 (1,1)에서 시작하여 (1,2)로 한 걸음 이동 후 (3,1)로 두 걸음 이동합니다.

안고홀 씨의 안전을 위해 n걸음 이 후의 좌표를 알려주는 함수를 정의하세요.
함수 이름은 triangular_walk로 하고 걸음 수 n이 입력으로 주어집니다.

midterm03_01.png

삼각수 규칙은 다음과 같습니다.
{1, 3, 6, 10, 15 ...}

midterm03_02.png

## 입력 설명
n 번째 걸음 수, n이 인자로 입력됩니다.

## 출력 설명
위치 좌표를 튜플로 반환합니다.


### 입력 예시 1 
1
### 출력 예시 1
(1,1)

### 입력 예시 2 
10
### 출력 예시 2
(4,1)

### 입력 예시 3 
100
### 출력 예시 3
(9,6)
"""""""""

def triangular_walk(n: int) -> tuple[int, int]:
    line = 0
    total_step = 0
    while total_step < n:
        line += 1
        total_step += line
        
    prev_step = total_step - line
    curr_step = n - prev_step
    if line % 2 == 0:
        row = curr_step
        col = line - curr_step + 1
    else:
        row = line - curr_step + 1
        col = curr_step
    return row, col


if __name__ == "__main__":
    arg1 = int(input())
    print(triangular_walk(arg1))
