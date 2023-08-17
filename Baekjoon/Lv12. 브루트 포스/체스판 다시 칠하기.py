## 문제 : 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
# B:검은색, W: 흰색

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
print(N, M)
print(board)

if N == M == 8:
    for row in board:
        print(row)
        if (row == 'WBWBWBWB') or (row == 'BWBWBWBW'):
            pass
        else:
            print(row)
                   
else:
    for row in board:
        print()
    




