## 문제 : 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.

n, m = map(int, input().split())
ball = list(range(1, n+1))

for _ in range(m):
    i, j = map(int, input().split())
    temp = ball[i-1]
    ball[i-1] = ball[j-1]
    ball[j-1] = temp

print(*ball)

# 다른 방법
n, m = map(int, input().split())
ball = list(range(1, n+1))

for _ in range(m):
    i, j = map(int, input().split())
    ball[i-1], ball[j-1] = ball[j-1], ball[i-1]

for x in ball:
    print(x, end =' ')
# 또는
print(' '.join(ball))