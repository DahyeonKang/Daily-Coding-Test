## 문제 : 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로

import sys
N = int(input())
li = list(set([sys.stdin.readline().strip() for _ in range(N)]))  # 중복 제거
li.sort()
li.sort(key=lambda x: len(x))
# li.sort(key=lambda x: (len(x), sorted(x)))
print(*li, sep='\n')  # sys.stdout.write(''.join(lst))

# 두개를 동시에 하는 건 안될까?
import sys
N = int(input())
li = list(set([sys.stdin.readline().strip() for _ in range(N)]))  # 중복 제거
li.sort(key=lambda x: (len(x), sorted(x)))
print(*li, sep='\n')