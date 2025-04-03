#1부터 N까지의 소수 개수를 출력하는 프로그램
n = int(input())
nprime = 0 #합성수의 개수 변수 setting
for i in range(2, n + 1):
    for k in range(2,i): #소수의 정의 참고
        if i % k == 0:
            nprime += 1
            break #중복으로 세기 방지 (6같은거)
print(n - nprime - 1) #1은 소수가 아니니까 빼주기