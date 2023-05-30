## 문제 : X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
# i 기준으로, 홀수 : 오른쪽(분모가 큼), 짝수 : 왼쪽(분자가 큼)에서 시작
# 1,  2,3  4,5,6  7,8,9,10  11,12,13,14,15   16,17,18,19,20,21
# 2     3    4       5             6                 7 : i
x = int(input())
i, sum = 0, 0
while x > sum:
    sum += i
    i += 1
temp = x - ((i-2)*(i-1)/2)  # 해당 구간에서 몇 번째인지
if i%2 == 0:  # 짝수, 왼쪽에서
    print('{0}/{1}' .format(int(i-temp), int(temp)))
else:  # 홀수, 오른쪽에서
    print('{0}/{1}' .format(int(temp), int(i-temp)))


# 다른 분 코드
n = int(input())
i = 1
while n>i:
    n-=i
    i+=1
if i%2==0:
    print(f"{n}/{i-n+1}")
else:
    print(f"{i-n+1}/{n}")
