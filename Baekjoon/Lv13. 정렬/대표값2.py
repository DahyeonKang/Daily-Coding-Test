## 문제 : 첫째 줄에는 평균을 출력하고, 둘째 줄에는 중앙값을 출력한다. 평균과 중앙값은 모두 자연수이다.

l = []
for _ in range(5):
    l.append(int(input()))
l.sort()
print(sum(l)//5)
print(l[2])

# 평균
import numpy as np
np.mean(l)
import statistics
statistics.mean(l)
# 중앙값
import numpy as np
np.median(l)
import statistics
statistics.median(l)
