## 문제 : 특이한 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

import string
alpha = string.ascii_uppercase
second = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,6,7,7,7,8,8,8,8]
str = input()
sum = 0
for i in range(len(str)):
    sum += (2+second[alpha.index(str[i])])
print(sum)