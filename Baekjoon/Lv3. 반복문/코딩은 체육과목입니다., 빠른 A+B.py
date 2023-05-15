## 문제 : 자료형 long int 이름 작성하기
# 코딩은 체육과목입니다.
n = int(input())
print('long '* (n//4) + 'int')



## 문제 : input()함수 말고 sys 함수의 입력 함수를 사용해서 합계를 출력하기
# 빠른 A+B

import sys
t = int(sys.stdin.readline())
for i in range(t):
    print(sum(map(int, sys.stdin.readline().split())))


