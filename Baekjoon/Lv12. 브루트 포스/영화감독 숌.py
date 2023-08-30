## 문제 : 숌이 만든 N번째 영화의 제목에 들어간 수를 출력하는 프로그램을 작성하시오. 숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.
# 666이 들어간 수들 중 작은 수를 찾는 문제.

# 666 앞과 뒤에 증가하는 수를 붙이려고 시도. But 너무 복잡하다..
# 수를 하나씩 증가시키면서 666이 포함됬는지 확인하는 게 빠름.

N = int(input())
target = '666'
i = 0
while N:
    i += 1
    if '666' in str(i):
        N -= 1
print(i)

# ex) 666 1666 2666 3666 4666 5666 6660 6661 6662 6663 ....
# 다른 분 코드
N = int(input())
li = []
n = 0
while len(li) <= N:
    if not n % 10 == 6:
        li.append(n*1000+666)
    elif (n//10) % 100 == 66:
        for k in range(1000):
            li.append(n*1000+k)
    elif (n//10) % 10 == 6:
        for j in range(100):
            li.append(n*1000+600+j)
    else:
        for i in range(10):
            li.append(n*1000+660+i)
    n += 1

print(li[N-1])
