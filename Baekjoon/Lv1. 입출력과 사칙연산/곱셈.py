## 문제 : 3자기 수 곱셈 과정의 중간 값들을 구하시오.

a = int(input())
b = int(input())
n_3 = a * (b % 10)
n_4 = a * (b % 100 // 10)
n_5 = a * (b % 1000 // 100)
print(n_3)
print(n_4)
print(n_5)
print(n_3+n_4*10+n_5*100)
# print(a*(b%10), a*((b//10)%10), a*(b//100), a*b, sep='\n')

# 다른 분 코드
a,b = int(input()),input()
print(*[a*int(p) for p in b][::-1], a*int(b))

# 다른 분 코드
B = B[::-1]
for i in B :
    print(A*int(i))
print(A*int(B[::-1]))
