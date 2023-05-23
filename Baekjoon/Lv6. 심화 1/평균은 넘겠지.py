## 문제 : 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

c = int(input())
for _ in range(c):
    count = 0
    l = list(map(int, input().split()))
    avg = sum(l[1:]) / l[0]
    # print(str(round(sum([count+1 for i in l[1:] if i>avg]) / l[0] * 100, 3)) + '%')
    percent = sum([count+1 for i in l[1:] if i>avg]) / l[0] * 100
    print(f'{percent:.3f}%')
