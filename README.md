# Python-FirstStep
A repository for learning the fundamentals of programming through Python

## 🗂️ 폴더 구조 및 파일 양식

### 폴더 구조
	.
	└── user-name					# 각 사용자의 이름을 사용한 폴더
		├── problems				# cnu judge 문제 탭에 게시된 문제들을 모아둔 폴더 
		│   	└── problem0000.py		# 문제 종류와 번호를 포함한 소스 코드 파일
		└── assignments				# 매주 업로드되는 과제들을 모아둔 폴더
			└── week00			# 주차별로 구분된 폴더
				└── asgmt00.py		# 문제 종류와 번호를 포함한 소스 코드 파일

### 파일 양식
- 소스 코드 상단에 문제명을 명시
- 코드 하단에 풀이 내용을 작성
- 풀이가 여러 개인 경우, 각각을 함수로 구분하여 관리
- 함수 형태로 작성해야 하는 문제는 `if __name__ == "__main__":` 블록 내에 정리
- 필요 시, 코드 하단에 문제 관련 메모를 추가

```python
# 글자 수 세기 함수
# 승인 완료

def count(word: str, target: str) -> int:
	return len([char for char in word if char == target])


def count1(word: str, target: str) -> int:
	cnt = 0
	for char in word:
		if char == target:
			cnt += 1
	return cnt


if __name__ == "__main__":
	str_, target = input().split()
	print(count(str_, target))

    
"""
memo
"""
```

## 🤝 Main repository에 기여하기

### 기여 순서
1. 소스 코드 작성 ([파일 양식](#파일-양식), [코드 작성 습관](#-코드-작성-습관) 참고)
2. 각 소스 코드마다 commit 메세지 작성 ([commit 작성 가이드](#-commit-작성-가이드) 참고)
3. remote repo에 push하기 전, main repo와 sync 후 pull
4. fork한 자신의 remote repo에 코드 push
5. 자신의 repo에서 `contribute` 버튼을 눌러 PR open
6. PR 설명란에 코드 설명을 상세히 작성 ([PR 과정 가이드](#-pr-과정-가이드) 참고)
7. PR이 승인되면, comment 확인 후 승인된 파일 상단에 `# 승인 완료` 주석 추가
8. PR이 거절(Request changes)되면, 수정 사항을 반영한 후 다시 comment 받기

## 🔧 commit 작성 가이드

### commit 메세지 형식
- `type: subject` (e.g. `feat: add week00/asgmt00`)

### Types
- `feat`: 새로운 기능 추가
- `fix`: 버그 수정 (해당 repo에서는 버그 수정보다 넓은 범위로 사용)
- `refactor`: 코드 리팩토링
- `chore`: 빌드 업무 수정, 패키지 매니저 변경, 패키지 관리자 구성 업데이트 등
- `docs`: 문서 내용 변경

### 작성 예시
#### 새로운 파일 추가
```
feat: add week00/asgmt00
```

#### 파일 수정
```
fix: edit week00/asgmt00
```

### 새로운 풀이 추가 
```
feat: add alternative solution to week00/asgmt00
```

## 💬 PR 과정 가이드

### 1. 새로운 PR 오픈
#### a. 제목 작성
```markdown
00/00 user-name file-name 1, file-name 2, ...
```

#### b. 양식에 맞추어 문제 풀이 작성
```markdown
### 📚 0주차 0번 - 문제명 or 추가 문제 0000번 - 문제명

#### 📝 문제 설명
- 문제의 전반적인 개요와 요구사항

#### 🔍 문제 해설
1. 단계 별 수행 목표
    - 구현 방법

#### 💡새로 알게 된 내용 & 배운 점
- 학습한 내용과 개선 포인트

#### ❓ 궁금한 점
- 추가로 논의하고 싶은 사항
```

#### c. 지난 PR에서 부여받은 Tasks 수행 후 기재 (지난 PR의 식별 번호 넣어서)
```markdown
### 🛠️ 과제 수행 #00(PR number)

#### Task 1(commit-id): task summary (code 관련 사항일 경우 commit id 기재)
- task 수행 내용 설명
- task 수행 내용 설명
```

#### d. `Preview` 버튼 눌러서 제대로 출력되는지 확인

### 2. 피드백 반영 (Request changes)
#### 피드백을 바탕으로 코드 수정 후, 수정 내용 반영된 commit id 기재하여 comment 추가
```markdown
000000(commit-id)

- 수정 사항 설명
- 수정 사항 설명
```

## 👨‍💻 코드 작성 습관

### Readability
- 어떻게 하면 간결한(readable) 코드를 짤 수 있을까?
- 주석 없이도 동작 과정이 잘 이해되는 코드가 좋은 코드 (타인의 시선에서 작성)
- 타인의 코드를 읽는 시간 늘리기 → 타인의 경험을 단기간에 습득 가능
- 언어마다 convention 지키기
- 직관적인 이름 짓기

### Efficiency
- 코드 작성 전 여러 가지 구현 방법 생각하기
- 가장 효율적인 방법으로 작성
- 작성 후에도 불필요한 코드가 없는지 확인

### 코드 작성 단계별 생각 정리
- 문제 정의 → 내가 수행하는 문제는 무엇인가? 잘게 쪼개어 생각
- 전 → 어떤 방법이 가장 효율적이며 과제를 문제없이 수행하는가?
- 후 → 작성한 코드의 불필요한 부분은 없는가? / 더 효율적인 방법이 없을까?
