## 문제 : 첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.
# 0 : 하얀색
# 1 : 파란색


import sys
N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = []

def solution(x, y, N) :
    color = paper[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != paper[i][j] :
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 0 :
        result.append(0)
    else :
        result.append(1)

solution(0, 0, N)
print(result.count(0))
print(result.count(1))






