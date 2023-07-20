## 문제 : 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

n = int(input())
list = list(map(int, input().split()))
count = 0
for i in list:
    if i != 1:
        for j in range(2, i+1):
            if i % j == 0:
                if j == i:
                    count += 1
                break
print(count)


# 아래는 틀린 코드 이유? 2 때문이다. 2가 두번쨰 for문에서 막혀서 다음 순서로 넘어간다.
for i in list:
    if i != 1:
        for j in range(2, i):
            if i % j == 0:
                break
            if j == i-1:
                count += 1


# 다른 분 코드
input()  # 쓰이지 않은 변수라 선언 불필요
l = list(map(int, input().split()))
cont = 0
for x in l:
    if x <= 1:
        continue
    for j in range(2, int(x ** 1/2)+1):
        if x % j == 0:
            break
    else:
        cont += 1
print(cont)