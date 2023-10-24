# 힙 사용
import heapq
# 편하게 하려고 deque 사용
from collections import deque
import sys


def solution(N, num_list):
    # 최대 힙
    max_heap = []
    # 최소 힙
    min_heap = []
    # deque, popleft 쓰려고..
    num_list = deque(num_list)
    
    i = 0
    while True:
        # 모두 넣으면 끝
        if not num_list:
            break
        # 홀수일 때는 max heap 에
        # max heap 이라 - 붙여서 입력
        if not i%2:
            heapq.heappush(max_heap, -num_list.popleft())
        # 짝수일 때는 min heap 에 번갈아서 넣어줌
        else:
            heapq.heappush(min_heap, num_list.popleft())
        # max heap 의 최댓값과 min heap 의 최솟값을 비교해서 교환
        # max heap 과 교환이라 - 붙여서 비교, 교환
        if i and -max_heap[0] > min_heap[0]:
            max_pop = -heapq.heappop(max_heap)
            min_pop = heapq.heappop(min_heap)
            
            heapq.heappush(max_heap, -min_pop)
            heapq.heappush(min_heap, max_pop)
            
        # i 증가
        i += 1
        # 출력
        # max heap 이라 - 붙여서 출력
        print(-max_heap[0])

            
N = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(N)]
solution(N, num_list)