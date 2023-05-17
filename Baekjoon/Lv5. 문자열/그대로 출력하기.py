## 문제 : 입력 받은 대로 출력하는 프로그램을 작성하시오.

import sys
for i in sys.stdin:
        print(i, end="")

# 다른 분 코드
import sys
print(''.join(sys.stdin.readlines()))


