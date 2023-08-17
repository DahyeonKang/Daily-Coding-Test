## 문제 : 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.


N = int(input())
l = []
for i in range(N, N//2-1, -1):
    if sum(map(int, str(i)))+i == N:
        l.append(i)
try:
    print(min(l))
except:
    print(0)

# 절반만 비교 vs 모든 경우의 수 비교
while True:
    N = int(input())
    l = []
    for i in range(N, N//2-1, -1):
        if sum(map(int, str(i)))+i == N:
            l.append(i)
    try:
        print(l)
    except:
        print(0)

    l = []
    for i in range(N, 0, -1):
        if sum(map(int, str(i)))+i == N:
            l.append(i)
    try:
        print(l)
    except:
        print(0)


# 다른 분 코드
# N-len(str(N))*9 : 생성자는 N을 두고 N의 각 자리수의 합을 빼주면 되는데
# 어떤 수가 올지 모르니까 최대수인 9를 자리수만큼 빼준다.
# 또 다른 분 코드를 보면, max 대신에 abs를 사용해서 N이 0~9일 때 음수인 경우를 제외할 수 있는 것 같다.
N = int(input())
ans = 0
for i in range(max(0, N-len(str(N))*9), N):
    if sum(map(int, str(i))) + i == N:
        ans = i
        break
print(ans)