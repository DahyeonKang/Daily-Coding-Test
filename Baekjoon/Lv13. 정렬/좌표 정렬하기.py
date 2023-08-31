## 문제 : 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 내 코드 - 실패 - 왜지?????????????? int를 str로 바꿔주지 않아서 그런건가?
import sys
n = int(input())
point = [sys.stdin.readline().split() for _ in range(n)]
point.sort()
for i in point:  # for i in range(0,9,2): print(" ".join(sum(point, [])[i:i+2]))
    print(" ".join(i))

# 내 코드 - 성공
import sys
n = int(sys.stdin.readline())
point = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
point.sort()
for i in point:
    print(i[0], i[1])  # join 사용하고 싶으면, print(" ".join(map(str, i)))

# 다른 분 코드 - 성공
N=int(input())
arr=[]
for i in range(N):
    a,b = map(int, input().split())
    arr.append((a, b))
print(arr)
arr.sort()
for i in range(N):
    print(arr[i][0], arr[i][1])

# 다른 분 코드 : sort 대신 lambda 이용
import sys
input = sys.stdin.readline
n = int(input())
dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))
dots.sort(key=lambda i: (i[0], i[1]))
for x, y in dots:
    print(x, y)

# 다른 분 코드 - 성공
import sys
n = int(sys.stdin.readline())
pos = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for line in sorted(pos):
    print(line[0],line[1])
    