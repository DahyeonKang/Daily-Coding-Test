## 문제 : n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# print(n*(n+1)//2)  # 다른 분 코드

## 예제 입력
# 3
## 예제 출력
# 6