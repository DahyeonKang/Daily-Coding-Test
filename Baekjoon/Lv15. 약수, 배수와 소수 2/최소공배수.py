## 문제 : 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(a, b)
    while True:
        result = max(a, b)
        if (result % a == 0) and (result % b == 0):
            print(result)
            break
        else:
            result += 1

# math 라이브러리 활용(파이썬 3.9 이상부터 가능)
# import math
# T = int(input())
# for _ in range(T):
#     a, b = map(int, input().split())
#     print(a, b)
#     print(math.lcm(a, b))