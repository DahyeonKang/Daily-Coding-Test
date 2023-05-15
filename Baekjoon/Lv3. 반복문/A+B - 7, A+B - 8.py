## 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# A+B - 8
import sys
T = int(input())
for i in range(1, T+1):
    print("Case #"+str(i)+":", sum(map(int, sys.stdin.readline().split())))


## 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# A+B - 8
import sys
T = int(input())
for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1} + {2} = {3}" .format(str(i), a, b, a+b))

## 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# A+B - 5
import sys
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a==0 and b==0:
        break
    print(a+b)


## 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# A+B - 4
import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break
# 다른 분 코드
import sys
for x in sys.stdin:
    a, b = map(int, x.split())
    print(a+b)
