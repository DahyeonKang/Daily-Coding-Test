## 문제 : 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

n, x = map(int, input().split())
a = list(map(int, input().split()))
print(*list(filter(lambda i: x > i, a)))

# 다른 분 코드
n, x = map(int, input().split())
answer = ' '.join([i for i in input().split() if int(i) < x])
print(answer, end='')

# 다른 분 코드
length, N = map(int, input().split())
nums = input().split()
for i in range(length):
    if int(nums[i]) < N:
        print(nums[i], end=' ')

## 입력
# 10 5
# 1 10 4 9 2 3 8 5 7 6
## 출력
# 1 4 2 3