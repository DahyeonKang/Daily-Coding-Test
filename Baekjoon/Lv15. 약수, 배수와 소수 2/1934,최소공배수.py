## 문제 : 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

# 내코드 - 실패 : 시간초과
# T = int(input())
# for _ in range(T):
#     a, b = map(int, input().split())
#     print(a, b)
#     while True:
#         result = max(a, b)
#         if (result % a == 0) and (result % b == 0):
#             print(result)
#             break
#         else:
#             result += 1

# math 라이브러리 활용(파이썬 3.9 이상부터 가능)
import math
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(a, b)
    print(math.lcm(a, b))

# 다른 분 코드 - 유클리드 호제법으로 최대공약수를 구하고 A, B의 곱을 최대 공약수로 나눠서 최소공배수 구하기
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    result = A*B
    while B>0:
        A,B = B, A%B
    print(result//A)