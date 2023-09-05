## 문제 : 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
S = []
for _ in range(N):
    S.append(sys.stdin.readline().strip())
M_l = []
for _ in range(M):
    M_l.append(sys.stdin.readline().strip())
print(sum([1 if i in S else 0 for i in M_l]))
# 마지막 print문 아래 주석문으로 대체 가능
# count = 0
# for i in M_l:
#     if i in S:
#         count += 1
#     else:
#         pass
# print(count)

# 다른 분 코드 : set 이용한 코드이고, 두번째 문자열 입력 때 비교도 동시에 해서 효율적이다.
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = set()
for i in range(N):
    S.add(input())
ans = 0
for _ in range(M):
    t = input()
    if t in S:
        ans+=1
print(ans)