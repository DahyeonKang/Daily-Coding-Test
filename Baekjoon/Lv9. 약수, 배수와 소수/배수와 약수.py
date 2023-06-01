## 문제 : 각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.

while 1:
    a, b = map(int, input().split())
    if a==0 & b==0:
        break
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')

# 다른 코드
while 1:
    try:
        a, b = map(int, input().split())
        if b % a == 0:
            print('factor')
        elif a % b == 0:
            print('multiple')
        else:
            print('neither')
    except:
        break


# 다른 분 코드
while True:
    a,b=map(int,input().split())
    if a==b==0:break
    print('factor'if b%a==0 else'multiple'if a%b==0 else'neither')