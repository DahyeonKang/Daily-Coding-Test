## 문제 : 이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때,
# 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록


# 최소힙과 최대힙 2개를 구현해 중복되는 값 출력 방법을 시도하려고 했지만 1번 테스트케이스에서 막힘!
import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    for i in operations:
        if i[:2] == 'I ':
            heapq.heappush(max_heap, -int(i[2:]))
            heapq.heappush(min_heap, int(i[2:]))
        try:
            if i == 'D 1':  # 최댓값 삭제
                heapq.heappop(max_heap)
            if i == 'D -1':  # 최솟값 삭제
                heapq.heappop(min_heap)
        except:
            pass
    print(max_heap, min_heap)
    max_heap = set(map(lambda x: x * (-1), max_heap))
    print(set(min_heap) & max_heap)




# 성공
import heapq
def solution(operations):
    min_heap = []
    for i in operations:
        if i[:2] == 'I ':
            heapq.heappush(min_heap, int(i[2:]))
        try:
            if i == 'D 1':  # 최댓값 삭제
                min_heap.pop()  # min_heap.remove(max(min_heap))
            if i == 'D -1':  # 최솟값 삭제
                heapq.heappop(min_heap)
        except:
            pass

    if not min_heap:
        return [0, 0]
    return [max(min_heap), min(min_heap)]



# heap의 최대값을 찾을 수 있는 nlargest, 최소값을 찾을 수 있는 nsmallest를 사용한 코드
import heapq
def solution(operations):
    heap = []

    for i in operations:
        op1, op2 = i.split()
        if op1 == 'I':
            heapq.heappush(heap, int(op2))
        elif heap:
            if op2 == "1":
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
            elif op2 == '-1':
                heapq.heappop(heap)
    if heap:
        min_value = heap[0]
        return [heapq.nlargest(1, heap)[0], min_value]
    else:
        return [0, 0]