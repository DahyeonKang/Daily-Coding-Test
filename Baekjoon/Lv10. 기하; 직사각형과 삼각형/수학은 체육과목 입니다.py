## 문제 : 한 변의 길이가 1인 정사각형을 아래 그림과 같이 겹치지 않게 빈틈없이 계속 붙여 나간다. 가장 아랫부분의 정사각형이 n개가 되었을 때, 실선으로 이루어진 도형의 둘레의 길이를 구하시오.

# 규칙 : 3+1, 3+3+2, 3+3+3+3, 3+3+3+3+4, 3+3+3+3+3+5, 3*6+6, 3*7+7
# 결론 : 4, 8, 12, 16, 20, 24, 28

n = int(input())
print(4*n)

