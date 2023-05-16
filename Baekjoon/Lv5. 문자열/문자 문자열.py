## 문제 : 단어 S,i가 주어졌을 때, S의 i번째 글자를 출력하는 프로그램을 작성하시오.

import sys
str = sys.stdin.readline()
i = int(sys.stdin.readline())
print(str[i-1])
