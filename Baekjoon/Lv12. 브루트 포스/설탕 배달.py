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
sugar = int(input())
bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print\
            (bag)
        break
    sugar -= 3
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)


