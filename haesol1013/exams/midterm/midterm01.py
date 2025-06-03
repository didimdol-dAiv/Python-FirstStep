"""""""""
# [50점] First In First Out (권장 풀이 시간: 10분)

## 설명
우리가 사용하는 운영체제에는 Stream Buffer(스트림 버퍼)라는 데이터 처리 체계가 있습니다.
Stream Buffer는 데이터가 들어오면 가장 먼저에 들어왔었던 데이터를 삭제하고 새로운 데이터를 채워넣습니다.
이러한 방식을 First In First Out(FIFO)라고 합니다.
1byte(8bit)로만 이루어진 스트림 버퍼가 있을 때, 새로운 데이터를 FIFO하는 함수를 정의하세요.
단, 함수 이름은 fifo로 합니다.

midterm01.png

허용 라이브러리: 없음

## 입력 설명
첫 번째 인자로 현재 데이터 값이 Integer로 입력됩니다.
두 번째 인자로 새로운 데이터 값이 String으로 입력됩니다.

## 출력 설명
새로운 데이터 값이 입력된 상태의 값을 Integer로 출력해야 합니다.


### 입력 예시 1 
51
"111"
### 출력 예시 1
159

### 입력 예시 2 
1
"1"
### 출력 예시 2
3

### 입력 예시 3 
3
"1"
### 출력 예시 3
7

### 입력 예시 4 
11
"101"
### 출력 예시 4
93

### 입력 예시 5 
1
"000"
### 출력 예시 5
8
"""""""""

def fifo(curr_data: int, new_data: str) -> int:
    ir = bin(curr_data)[2:] + new_data
    return int(ir[-8:], 2)


if __name__ == "__main__":
    arg1 = int(input())
    arg2 = input()[1:-1]
    print(fifo(arg1, arg2))
