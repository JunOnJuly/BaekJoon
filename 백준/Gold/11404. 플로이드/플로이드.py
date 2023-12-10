import sys


def solution(n, data_list):
    # 최대 거리
    inf = float('inf')
    # 거리 맵 구성, [i][j] 는 i 에서 j 로 가는 최단 거리
    dist_map = [[inf for _ in range(n+1)] for __ in range(n+1)]
    # 데이터 거리 맵에 입력
    for start, end, dist in data_list:
        if dist < dist_map[start][end]:
            dist_map[start][end] = dist
    # 자기 자신까지의 거리는 0
    for i in range(1, n+1):
        dist_map[i][i] = 0
    # 중간점
    for mid in range(1, n+1):
        # 시작점
        for start in range(1, n+1):
            # 끝점
            for end in range(1, n+1):
                # 중간점을 지나는 모든 거리 비교
                dist_map[start][end] = min(dist_map[start][mid]+dist_map[mid][end], dist_map[start][end])
    # 도달 못하는 인덱스 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist_map[i][j] == inf:
                dist_map[i][j] = 0
                
    for line in range(1, n+1):
        print(*dist_map[line][1:])


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
data_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
solution(n, data_list)