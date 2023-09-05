## 문제 : 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# 내 코드 - 성공: list를 set으로 바꿨을 뿐인데 성공!
import sys
N = int(sys.stdin.readline())  # 상근 카드 개수
num = set(map(int, sys.stdin.readline().split())) # 숫자 카드에 적혀있는 정수들(중복 X)
M = int(sys.stdin.readline())  # 확인할 카드 개수
test = map(int, sys.stdin.readline().split())  # 확인할 카드 정수들

for i in test:
    if i in num:
        print(1, end=" ")
    else:
        print(0, end=" ")
# for 문 아래로 대체 가능
# for i in range(M):
#     if test[i] in num:
#         print(1, end=" ")
#     else:
#         print(0, end=" ")


# 내 코드 - 시간 초과 실패: for문이 시간복잡도가 O(n)이라서 시간 초과 유발.
# tip : set()는 O(n)이다. 따라서 list를 set으로 바꾸면 시간 초과 해결 가능.
# import sys
# N = int(sys.stdin.readline())
# num = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# test = map(int, sys.stdin.readline().split())
#
# for i in test:
#     if i in num:
#         print(1, end=" ")
#     else:
#         print(0, end=" ")


# 다른 분 코드 : 다른 건 비슷하지만 마지막줄 print구문이 간결하다. for, if문을 list comprehension에서 사용할 수 있다.
N = input()
s = set(input().split())
M = input()
print(" ".join(["1" if i in s else "0" for i in input().split()]))