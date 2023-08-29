## 문제 : 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
# B:검은색, W: 흰색

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
result = []
# N, M = map(int, input().split())
# board = []
# result = []
# for _ in range(N):
#     board.append(input())

for i in range(N-7):
    for j in range(M-7):
        is_it_black = 0
        is_it_white = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'B':
                        is_it_black += 1
                    if board[a][b] != 'W':
                        is_it_white += 1
                else:
                    if board[a][b] != 'W':
                        is_it_black += 1
                    if board[a][b] != 'B':
                        is_it_white += 1

        result.append(is_it_black)
        result.append(is_it_white)
print(result)
print(min(result))



