# def countBetween(arr, low, high):
#     n = len(low)
#     answer = [0] * n
#     for i in arr:
#         for j in range(n):
#             if low[j]<=i<=high[j]:
#                 answer[j] += 1
#     return answer
#
# def countBetween(arr, low, high):
#     n = len(arr)
#     m = len(high)
#     answer = [0] * m
#     i, j = 0, 0
#     while i>n and j>m:
#         if low[j] <= arr[i] <= high[j]:
#             answer[j] += 1
#         elif arr[i] < low[j]:
#             i += 1
#         else:
#             j += 1
#     return answer
#
# import bisect
# def countBetween(arr, low, high):
#     n = len(arr)
#     m = len(low)
#     answer = [0] * m
#
#     # 정렬된 arr 리스트를 입력으로 받았다고 가정합니다.
#     arr.sort()
#
#     for i in range(m):
#         # low와 high 사이에 있는 arr 값 개수를 세기 위해 이진 탐색을 사용합니다.
#         left_index = bisect.bisect_left(arr, low[i])
#         right_index = bisect.bisect_right(arr, high[i])
#         answer[i] = right_index - left_index
#
#     return answer
#
#
# print(countBetween([1,2,2,3,4],[0,2],[2,4]))

# def dfs(G, v, visited, V):
#     visited[v] =  True
#     V.append(v)
#     for i in G[v]:
#         if not visited[i]:
#             dfs(G, v, visited)
#
# def tasks(n, l, G, v, visited):
#     i = 0
#     V = []
#     while G[i]:
#         i += 1
#         if G[i]:
#             dfs(G, i, visited, V)
#     print(V)
#
#
#
#
# n = 7
# a = [1,2,3,4,6,5]
# b = [7,6,4,1,2,1]
# visited = [True] + [False] * n
# minus = 0
# G = [[] for _ in range(n+1)]
# for i, j in zip(a, b):
#     G[j].append(i)
# print(G)
# print(dfs(n, a, b, G, 1, minus))


import math
import os
import random
import re
import sys





# def tasks(n, G, visited, visit):
#     global minus
#     i = 0
#     minus = 0
#     while G[i]:
#         i += 1
#         if G[i]:
#             dfs(G, i, visited, visit)
#     print(minus)
#     return visited, visit

def dfs(graph, v, visited, visit, minus):
    visited[v] = True
    visit.append(v)
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, visit, minus)
        elif visited[i] and v in graph[i]:
            minus += 1


n = int(input().strip())
a_count = int(input().strip())
a = []
for _ in range(a_count):
    a_item = int(input().strip())
    a.append(a_item)

b_count = int(input().strip())
b = []
for _ in range(b_count):
    b_item = int(input().strip())
    b.append(b_item)


visited = [True] + [False] * n
G = [[] for _ in range(n + 1)]
for i, j in zip(a, b):
    G[j].append(i)
minus, i = 0, 0
visit = []

while True:
    i += 1
    if i < (n+1):
        if G[i]:
            print(dfs(G, i, visited, visit, minus))
    else:
        break

