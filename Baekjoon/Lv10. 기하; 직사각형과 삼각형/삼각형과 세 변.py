## 문제 : 삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.
# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우
# 단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다.
# 세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    long = max(a, b, c)
    if long < (a+b+c-long):
        if a == b == c:
            print("Equilateral")
        elif (a==b) | (b==c) | (c==a):
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")


# 다른 분 코드 : 리스트 인덱싱을 이용한
while 1:
    li = sorted(list(map(int, input().split())))
    if li[0] == li[1] == li[2] == 0:
        break
    if li[0]+li[1] <= li[2]:
        print("Invalid")
    elif li[0] == li[1] == li[2]:
        print("Equilateral")
    elif li[0]==li[1] or li[1]==li[2] or li[2]==li[0]:
        print("Isosceles")
    else:
        print("Scalene")


