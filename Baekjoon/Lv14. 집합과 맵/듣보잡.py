## 문제 : 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

N, M = map(int, input().split())
nohear = []
nosee = []
for _ in range(N):
    nohear.append(input())
for _ in range(M):
    nosee.append(input())

both = set(nohear).intersection(nosee)
print(len(both))
print(*sorted(both), sep='\n')


# 다른 분 코드 : 내코드 더 간단하게 구현한 코드
import sys
a,b = map(int, sys.stdin.readline().strip().split())
arr = sys.stdin.read().strip().split()
arr = sorted(list(set(arr[:b]) & set(arr[b:])))
print(len(arr), '\n'.join(arr), sep='\n')