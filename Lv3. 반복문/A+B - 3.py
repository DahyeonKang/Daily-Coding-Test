## 문제 : A+B를 여러 번 출력하는 문제

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(a + b)


## 예제 입력
# 5
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2
## 예제 출력
# 7
# 2
# 5
# 7
# 17
