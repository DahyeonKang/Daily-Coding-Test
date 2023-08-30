## 문제 : 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

N = int(input())
l = []
for i in range(0, N//5+2):
    for j in range(0, N//3+2):
        if 5*i + 3*j == N:
            l.append(i+j)
try:
    print(min(l))
except:
    print(-1)

# 다른 분 코드
x = int(input())
a = 0
while x >= 0:
    if x % 5 == 0:
        a += (x//5)
        print(a)
        break
    x = x - 3
    a = a + 1
else:
    print(-1)


