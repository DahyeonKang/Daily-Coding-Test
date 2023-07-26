## 문제 : 삼각형의 세 각을 입력받은 다음,
# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
# 를 출력하는 프로그램을 작성하시오.

a = int(input())
b = int(input())
c = int(input())

if a == b == c == 60:
    print("Equilateral")
elif (a+b+c) == 180:
    if (a==b) | (b==c) | (a==c):
        print("Isosceles")
    else:
        print("Scalene")
elif (a+b+c) != 180:
    print('Error')


# 다른 분 코드
if a+b+c == 180:
    if a==b and b==c:
        print('Equilateral')
    elif a==b or b==c or a==c:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')

# 다른 분 코드
p = print
tr = [int(input()) for _ in range(3)]
if all(i == 60 for i in tr):
    p('Equilateral')
elif (s:=sum(tr) == 180) and len(set(tr)) == 2:
    p('Isosceles')
elif s:
    p('Scalene')
else:
    p('Error')