import sys
import heapq
from bisect import insort

input = sys.stdin.readline


def solution(k, querys):
    # 최대 / 최소 힙
    max_heap = []
    min_heap = []
    # 동기화를 위한 삭제 체크
    deleted = [False for _ in range(k)]
    # 쿼리 순회
    for q in range(k):
        # 쿼리
        query = querys[q]
        # 삽입
        if query[0] == 'I':
            # 큐에 삽입
            heapq.heappush(min_heap, [int(query[1]), q])
            heapq.heappush(max_heap, [-int(query[1]), q])
        
        # 삭제
        else:
            # 최소
            if query[1] == '1':
                # 반복
                while max_heap:
                    # 삭제된 수, 쿼리 인덱스
                    deleted_num, query_idx = heapq.heappop(max_heap)
                    # 이미 삭제된 인덱스면
                    if deleted[query_idx]:
                        # 다시
                        continue
                    
                    # 삭제되지 않은 인덱스면
                    else:
                        # 삭제 기록
                        deleted[query_idx] = True
                        # 끝
                        break
            
            # 최대
            else:
                # 반복
                while min_heap:
                    # 삭제된 수, 쿼리 인덱스
                    deleted_num, query_idx = heapq.heappop(min_heap)
                    # 이미 삭제된 인덱스면
                    if deleted[query_idx]:
                        # 다시
                        continue
                    
                    # 삭제되지 않은 인덱스면
                    else:
                        # 삭제 기록
                        deleted[query_idx] = True
                        # 끝
                        break

    # 큐 병합
    queue = []
    for num, idx in max_heap:
        # 삭제되지 않은 수만 큐에 삽입
        if not deleted[idx]:
            queue.append(-num)
    
    if not queue:
        print('EMPTY')
    
    else:
        print(f'{max(queue)} {min(queue)}')


# 입력
T = int(input().strip())
for _ in range(T):
    k = int(input().strip())
    querys = [list(input().strip().split()) for _ in range(k)]
    
    solution(k, querys)