import sys
import heapq


def solution(N, data_list):
    # 최대힙, 최소힙
    max_heap = []
    min_heap = []
    # 음수는 최대힙에 넣고 양수는 최소힙에 넣음
    for data in data_list:
        # 입력이 0 이면
        if not data:
            # 둘 다 비어있으면 0
            if not max_heap and not min_heap:
                print(0)
            # 최대힙만 차있으면
            elif max_heap and not min_heap:
                print(-heapq.heappop(max_heap))
            # 최소힙만 차있으면
            elif min_heap and not max_heap:
                print(heapq.heappop(min_heap))
            # 둘 다 있으면
            else:
                # 최소힙[0]의 절댓값이 작으면
                if min_heap[0] < max_heap[0]:
                    print(heapq.heappop(min_heap))
                # 최대힙[0]의 절댓값이 작으면
                # 최대힙의 데이터는 음수라 무조건 최소힙의 데이터보다 작으므로 절댓값이 같아도
                else:
                    print(-heapq.heappop(max_heap))
        # 입력이 0 이 아니면
        else:
            # 입력이 양수면 최소힙에 푸시
            if data > 0:
                heapq.heappush(min_heap, data)
            # 입력이 음수면 최대힙에 푸시
            else:
                heapq.heappush(max_heap, -data)


N = int(sys.stdin.readline())
data_list = [int(sys.stdin.readline()) for _ in range(N)]
solution(N, data_list)