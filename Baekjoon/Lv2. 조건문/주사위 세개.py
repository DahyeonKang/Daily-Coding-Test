## 문제 : 주사위 세개를 던져서 같은 눈을 가진 개수에 따라 상금을 계산하기

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a*1000)
elif a != b and b != c and a != c:
    print(max(a, b, c)*100)
else:
    i = [x for i,x in enumerate([a,b,c]) if i != [a,b,c].index(x)]
    print(1000 + int(i[0])*100)
    

# 다른 분 코드
a,b,c=map(int,input().split())

if(a==b==c):
    print(10000+a*1000)
elif a==b or a==c:
    print(1000+a*100)
elif b==c:
    print(1000+b*100)
else:
    print(max(a,b,c)*100)