## 문제 : n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

while True:
    n = int(input())
    if n == -1:
        break
    div = [i for i in range(1, n) if n%i==0]
    if n == sum(div):
        print("{} =" .format(n), " + ".join(map(str, div)))
    else:
        print("{} is NOT perfect." .format(n))
