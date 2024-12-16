import sys

input = sys.stdin.readline


def solution(N, M, edges, querys):
    ### 최단거리 업데이트
    ## 플로이드-워셜
    # 거쳐갈 노드
    for mid in range(N):
        # 출발 노드
        for start in range(N):
            # 끝 노드
            for end in range(N):
                edges[start][end] = min(edges[start][end], edges[start][mid] + edges[mid][end])
    
    # 쿼리 처리
    for A, B, C in querys:
        # 시간 비교
        if edges[A-1][B-1] <= C:
            print('Enjoy other party')
        
        else:
            print("Stay here")


# 입력
N, M = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(N)]
querys = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, edges, querys)