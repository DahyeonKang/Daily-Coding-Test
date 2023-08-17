## 문제 : 연립방정식의 해 x,y를 공백으로 구분해 출력한다.

import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split())
y = int((c/a - f/d) / (b/a - e/d))
x = int((c - b*y) / a)
print(x, y)