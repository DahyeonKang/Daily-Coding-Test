## 문제 : 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
# 두 수 비교하기
a, b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')

# 다른 분 코드
print(">" if a>b else "<" if a<b else "==")

## 문제 : 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# 시험 성적년
score = int(input())
if (score>=90) & (score<=100):
    print('A')
elif (score>=80) & (score<90):
    print('B')
elif (score>=70) & (score<80):
    print('C')
elif (score>=60) & (score<70):
    print('D')
else:
    print('F')

# 다른 분 코드
a=int(input())
if a < 60:
    print('F')
elif a < 70:
    print('D')
elif a < 80:
    print('C')
elif a < 90:
    print('B')
else:
    print('A')

# 다른 분 코드
a = int(input())
if 90 <= a <= 100:
    print("A")
elif 80 <= a <= 89:
    print("B")
elif 70 <= a <= 79:
    print("C")
elif 60 <= a <= 69:
    print("D")
else:
    print("F")

# 다른 분 코드
print('FFFFFFDCBAA'[int(input())//10])