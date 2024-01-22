
# 입력과 출력을 자유롭게 작성해주세요

def f(low, col):
    # 내가 밟은 자리는 방문함 처리
    visit[low][col] = n

    # 범위 안, 방문, 섬?
    if co l +1 < w and visit[low][co l +1] == 0 and arr[low][co l +1] == 1:
        f(low ,co l +1)
    if co l -1 >= 0 and visit[low][co l -1] == 0 and arr[low][co l -1] == 1:
        f(low ,co l -1)
    if lo w +1 < h and visit[lo w +1][col] == 0 and arr[lo w +1][col] == 1:
        f(lo w +1 ,col)
    if lo w -1 >= 0 and visit[lo w -1][col] == 0 and arr[lo w -1][col] == 1:
        f(lo w -1 ,col)

w, h = map(int, input().split())

arr = []
for i in range(h):
    arr.append(list(map(int ,input().split())))
# 방문체크
visit = [[0 for i in range(w) ]for j in range(h)]

n = 0
for i in range(h):
    for j in range(w):
        # 방문한적 없는지?, 섬인지
        if visit[i][j] == 0 and arr[i][j] == 1:
            n += 1
            f(i ,j)

print(n)







### 조건문 간단히 한 코드
def f(low, col):
    # 내가 밟은 자리는 방문함 처리
    visit[low][col] = n

    # 범위 안, 방문, 섬?

    l = [0, 0, 1, -1]
    c = [1, -1, 0, 0]

    for i in range(4):
        nl = low + l[i]
        nc = col + c[i]
        # 범위 안에 있는가?
        if 0 <= nl < h and 0 <= nc < w:
            # 방문한적 없는가?, 섬인가?
            if visit[nl][nc] == 0 and arr[nl][nc] == 1:
                f(nl, nc)


w, h = map(int, input().split())

arr = []
for i in range(h):
    arr.append(list(map(int, input().split())))
# 방문체크
visit = [[0 for i in range(w)] for j in range(h)]

n = 0
for i in range(h):
    for j in range(w):
        # 방문한적 없는지?, 섬인지
        if visit[i][j] == 0 and arr[i][j] == 1:
            n += 1
            f(i, j)

print(n)