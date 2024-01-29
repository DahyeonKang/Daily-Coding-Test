## 문제 : Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return


# 성공 1
def solution(brown, yellow):
    total = brown + yellow
    rows = [(total) // c for c in range(3, (total)//3 + 1) if (total) % c == 0]
    for row in rows:
        col = (total) // row
        if 2*(row+col-2) == brown:
            return [row, col]


# 성공 2
def solution(brown, yellow):
    sum = brown + yellow
    for i in range(1, sum):
        if sum % i == 0:  # 약수임
            w = max(i, sum // i)
            h = min(i, sum // i)
            if (w - 2) * (h - 2) == yellow and (2 * (w + h) - 4) == brown:
                return [w, h]

# 성공 2를 아래 코드에 따라 코친 코드
def solution(brown, yellow):
    S = brown + yellow
    for i in range(1, int(S ** 0.5) + 1):
        if S % i == 0:  # 약수임
            w = S // i
            h = i
            if (w - 2) * (h - 2) == yellow and (2 * (w + h) - 4) == brown:
                return [w, h]


# 성공 2 코드에서 시간 줄이는 방법 - 반복문을 절반 정도만 하는 것이다.
def solution(brown, yellow):
    mn = brown + yellow
    for m in range(3, int(mn ** 0.5) + 1):
        if mn % m == 0 and 2 * (mn // m + m - 2) == brown:
            return [mn // m, m]