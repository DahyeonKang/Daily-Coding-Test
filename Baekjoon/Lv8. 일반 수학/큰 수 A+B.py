## 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 9223372036854775807 9223372036854775808 -> 18446744073709551615

import sys
print(sum(map(int, sys.stdin.readline().split())))
