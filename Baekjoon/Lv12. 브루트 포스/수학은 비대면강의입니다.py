## 문제 : 연립방정식의 해 x,y를 공백으로 구분해 출력한다.

import sys
# 가감법 이용 코드
a, b, c, d, e, f = map(int, sys.stdin.readline().split())
x = (c*e-b*f)//(a*e-b*d)
y = (c*d-a*f)//(b*d-a*e)
print(x, y)

# 브루트포스 알고리즘 이용 코드
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x+b*y == c and d*x+e*y == f:
            print(x, y)
            break

## 처음에 시도했던 코드 실패 이유 : 가감법과 똑같은 의미긴한데 나누기가 많이 잇어서 x,y가 무조건 정수여야
# 하는 해당 문제에서는 답이 다르게 나온다.
# y = (c/a - f/d) / (b/a - e/d)
# x = (c - b*y) / a
# print(x, y)
