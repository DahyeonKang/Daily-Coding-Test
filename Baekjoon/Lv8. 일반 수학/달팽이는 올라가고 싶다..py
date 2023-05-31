## 문제 : 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.
# 높이 V, 낮에 A 위로, 밤에 B 아래로, 정상에 올라간 뒤로 미끄러지지 않음.

# 2 1 5 -> 4
# 5 1 6 -> 2
# 5 4 7 -> 2
# 100 99 1000000000 -> 999999901

import math
a, b, v = map(int, input().split())
print(math.ceil((v-b) / (a-b)))
# rest = v % (a-b)
# if rest == 0:
#     print(v // (a-b) - b)
# else:
#     print(v // (a-b) + b)

# 다른 분 코드
a, b, h = map(int, input().split())
print((h-b-1)//(a-b)+1)
