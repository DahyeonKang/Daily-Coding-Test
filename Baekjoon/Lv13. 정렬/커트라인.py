## 문제 : 상을 받는 커트라인을 출력하라.

N, k = map(int, input().split())
score = list(map(int, input().split()))
score.sort(reverse=True)
print(score[k-1])