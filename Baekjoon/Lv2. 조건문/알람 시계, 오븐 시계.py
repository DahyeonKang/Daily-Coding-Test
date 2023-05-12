## 뮨제 : 입력된 시간/분에서 45분 앞서는 시간으로 변환하기
# 알람 시계
h, m = map(int, input().split())
if m - 45 < 0:
    if h == 0: print(23, 60 - 45 + m)
    else: print(h - 1, 60 - 45 + m)
else:
    print(h, m - 45)


# 다른 분 코드
H, M = map(int, input().split())
print(((H*60+M-45)//60)%24, (M-45)%60)


## 문제 : 입력된 시간/분에서 C분 늦는 시간으로 변환하기
# 오븐 시계
A, B = map(int, input().split())
C = int(input())
print(((A*60+B+C)//60)%24, (B+C)%60)

