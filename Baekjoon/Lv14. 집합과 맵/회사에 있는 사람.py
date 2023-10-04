## 문제 : 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.

# import sys
# n = int(sys.stdin.readline())
# L = list()
# for _ in range(n):
#     L.append(sys.stdin.readline().split())
# D = dict(L)
# print("\n".join(sorted([k for k, v in D.items() if v == 'enter'], reverse=True)))


# 다른 분 코드
import sys
input = sys.stdin.readline
N = int(input())
company = {}
for _ in range(N):
    man, state = input().rstrip().split()
    if state == "enter":
        company[man] = True
    else:
        del company[man]
print("\n".join(sorted(company.keys(), reverse=True)))

