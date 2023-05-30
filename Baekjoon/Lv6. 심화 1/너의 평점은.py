## 문제 : 치훈이의 전공평점을 구하는 프로그램을 만드시오. 정답과의 절대오차 또는 상대오차가 \(10^{-4}\) 이하이면 정답으로 인정한다.

sum = 0
sumnum = 0
table = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
for _ in range(20):
    subject, score, grade = input().split()
    if grade != 'P':
        sumnum += float(score)
        sum += float(score) * table[grade]
print('{:.6f}' .format(sum/sumnum))


# import sys
# try:
#     for i in sys.stdin:
#         if i != '':
#             subject = i.split()
#             if subject[2] != 'P':
#                 grade.append(subject[2])
#                 num.append(float(subject[1]))
# except :
#     grade = [score[i] for i in grade]
#     print('{:.6f}'.format(sum(list(map(lambda x, y: x * y, num, grade))) / sum(num)))

