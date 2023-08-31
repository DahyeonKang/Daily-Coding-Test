## 문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# sort()함수가 메모리 초과 유발 -> 계수정렬 사용
# input()함수가 시간 초과 유발 -> sys 함수 사용

import sys
N = int(sys.stdin.readline())
count = [0] * 10000
# 입력된 수 크기만큼 수 입력받기
for i in range(N):
    num = int(sys.stdin.readline())
    count[num-1] += 1  # (입력수에 해당하는 위치-1)에 수의 개수를 넣는다. ex) 1이 입력수이면 count[0]에 1 더하기.
# 오름차순으로 출력하기
print(count)
for i in range(10000):
    if count[i] != 0:  # 수가 있을 때
        for j in range(count[i]):
            print(i+1)

