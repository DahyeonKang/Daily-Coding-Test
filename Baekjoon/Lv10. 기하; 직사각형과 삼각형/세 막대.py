## 문제 : a, b, c가 주어졌을 때, 만들 수 있는 가장 큰 둘레를 구하는 프로그램을 작성하시오.

l = list(map(int, input().split()))
if max(l) < sum(l) - max(l):
    print(sum(l))
else:
    print(sum(l) - max(l) + (sum(l) - max(l) - 1))


# 다른 분 코드 : 리스트 이용
l = sorted(list(map(int,input().split())))
print(min(sum(l), 2*(l[0]+l[1])-1))

# 다른 분 코드 : 리스트 이용 X
a,b,c=sorted(map(int,input().split()))
print(a+b+min(c,a+b-1))