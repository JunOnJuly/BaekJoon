import sys


def solution(V, E, data_list):
    # 최대 거리
    inf = float('inf')
    # 거리 맵
    dist_map = [[inf for _ in range(V+1)] for __ in range(V+1)]
    # 데이터 입력
    for start, end, dist in data_list:
        dist_map[start][end] = dist
    # 플로이드 워셜
    # 중간점
    for mid in range(1, V+1):
        # 시작점
        for start in range(1, V+1):
            # 끝점
            for end in range(1, V+1):
                # 최단거리 최신화
                dist_map[start][end] = min(dist_map[start][end], dist_map[start][mid]+dist_map[mid][end])
    # 최단 루프
    min_loop = inf
    # 최단 루프 탐색
    for start in range(1, V+1):
        for end in range(1, V+1):
            if start != end:
                min_loop = min(min_loop, dist_map[start][end] + dist_map[end][start])
    print(min_loop if min_loop < inf else -1)


V, E = map(int, sys.stdin.readline().strip().split())
data_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(E)]
solution(V, E, data_list)