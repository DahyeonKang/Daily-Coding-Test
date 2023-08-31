## 문제 : 첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

import sys
N = int(input())
li = [sys.stdin.readline().split() for _ in range(N)]
li.sort(key=lambda x: int(x[0]))  # int() 안하면 틀림
for i in li:
    print(" ".join(i))

# # 실패한 코드 이유 : 나이가 꼭 2글자일리는 없다. :2를 단정지으면 안된다.
# import sys
# N = int(input())
# li = [sys.stdin.readline().split() for _ in range(N)]
# print(li)
# li.sort(key=lambda x: x[:2])
# print("\n".join(li))

# 다른 분 코드
import sys
print(''.join(sorted(sys.stdin.readlines()[1:], key= lambda x: int(x.split()[0]))))