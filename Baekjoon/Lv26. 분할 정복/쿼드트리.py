## 문제 : 쿼드트리의 규칙대로 영상을 압축한 결과를 출력한다.

import sys

N = int(input())
video = [ list(map(int, list(sys.stdin.readline().rstrip("\n")) )) for _ in range(N)]
result = ""
def solution(x, y, N):
    global result
    first = video[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if first != video[i][j]:
                result += "("
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                result += ")"
                return
    result += str(first)

solution(0, 0, N)
print(result)