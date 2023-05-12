## 문제 : 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년
year = int(input())
if year%4 == 0 and (year%100 != 0 or year%400 == 0):
    print(1)
else:
    print(0)

## 문제 : 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오.
# 사분면 고르기
x = int(input())
y = int(input())
if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)

# 다른 분 코드
x = int(input())
y = int(input())
print("3421"[x>0::2][y>0])
# 설명 : 비교로 True/False 값을 1/0으로 대체되는 것을 이용한 extended slices 방법

