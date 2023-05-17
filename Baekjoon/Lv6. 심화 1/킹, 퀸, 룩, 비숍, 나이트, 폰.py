## 문제 : 동혁이가 발견한 흰색 피스의 개수가 주어졌을 때, 몇 개를 더하거나 빼야 올바른 세트가 되는지 구하는 프로그램을 작성하시오.

l = list(map(int, input().split()))
correct = [1, 1, 2, 2, 2, 8]
print(*[a-b for a, b in zip(correct, l)])

# 다른 분 코드
k,q,l,b,i,p=map(int,input().split())
print(1-k,1-q,2-l,2-b,2-i,8-p)
