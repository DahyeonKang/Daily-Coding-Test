## 문제 : 첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를,
# 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.


import sys
N = int(input())
paper = [ list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

result = []
def solution(x, y, N):
    first = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if first != paper[i][j]:
                solution(x, y, N//3)
                solution(x, y+N//3, N//3)
                solution(x, y+N//3+N//3, N//3)
                solution(x+N//3, y, N//3)
                solution(x+N//3, y+N//3, N//3)
                solution(x+N//3, y+N//3+N//3, N//3)
                solution(x+N//3+N//3, y, N//3)
                solution(x+N//3+N//3, y+N//3, N//3)
                solution(x+N//3+N//3, y+N//3+N//3, N//3)
                return
    if first == 0:
        result.append(0)
    elif first == -1:
        result.append(-1)
    else:
        result.append(1)

solution(0, 0, N)
print(result.count(-1))
print(result.count(0))
print(result.count(1))



# 다른 분 코드
import sys

n = int(input())
paper = []
paper = [ list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

result = {-1:0, 0:0,1:0}

def divided(row,col,n):
    curr = paper[row][col] # 종이의 시작

    for i in range(row, row+n):
        for j in range(col, col+n):
            # 현재 종이 종류와 다르다면
            if paper[i][j] != curr:
                next = n//3
                # 종이를 같은 크기의 종이 9개로 자르므로
                divided(row, col, next) # 1번째 block (0,0)
                divided(row, col+next, next) # 2번째 block (0,1)
                divided(row, col+(next*2), next) # 3번째 block (0,2)
                divided(row+next, col, next) # 4번째 block (1,0)
                divided(row+next, col+next, next) # 5번째 block (1,1)
                divided(row+next, col+(next*2), next) # 6번째 block (1,2)
                divided(row+(next*2), col, next) # 7번째 block (1,0)
                divided(row+(next*2), col+next, next) # 8번째 block (1,1)
                divided(row+(next*2), col+(next*2), next) # 9번째 block (1,2)
                return
    result[curr] +=1
    return

divided(0,0,n)
for i in result.values():
    print(i)


# dfs로 푸신 분
import sys


def dfs(x, y, z):
    global answer
    visited = graph[x][y]

    # 반복문을 통해 종이를 확인
    for i in range(x, x + z):
        for j in range(y, y + z):
            # 시작점에 종이의 수가 현재 종이의 수와 다르다면
            if graph[i][j] != visited:
                # 3 * 3 범위를 재귀적으로 탐색
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * z // 3, y + l * z // 3, z // 3)
                return

    # 카운트
    if visited == -1:
        answer[0] += 1
    elif visited == 0:
        answer[1] += 1
    else:
        answer[2] += 1


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = [0, 0, 0]
dfs(0, 0, n)
[print(res) for res in answer]
