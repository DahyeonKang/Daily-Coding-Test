## 문제 : 첫째 줄부터 N개의 줄에 행렬 A와 B를 곱한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

import sys
N, M = map(int, input().split())
A_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M, K = map(int, input().split())
B_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
R_matrix = [[0]*K for _ in range(N)]

for i in range(N):
    for j in range(K):
        temp = 0
        for m in range(M):
            temp += A_matrix[i][m] * B_matrix[m][j]
        R_matrix[i][j] = temp

for i in R_matrix:
    print(*i)