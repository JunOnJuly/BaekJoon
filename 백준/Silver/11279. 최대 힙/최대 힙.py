import heapq
import sys


def solution(N, data_list):
    # 큐
    hq = []
    # 순차적으로 진행
    for data in data_list:
        # 0 이면
        if not data:
            # 큐가 비어있으면
            if not hq:
                print(0)
            # 아니면
            else:
                print(-heapq.heappop(hq))
        # 0 이 아니면
        else:
            heapq.heappush(hq, -data)
    
    
N = int(sys.stdin.readline().strip())
data_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
solution(N, data_list)