import heapq


def solution(N, M, data_list):
    # 시스템상 최댓 값
    inf = float('INF')
    # 비용 맵
    weight_map = [[inf for _ in range(M)] for __ in range(N)]
    # 시작 위치, 비용 맵 정리
    start = []
    for idx in range(len(data_list[0])):
        start.append([data_list[0][idx], [0, idx], 9])
        weight_map[0][idx] = data_list[0][idx]
    # 다익스트라..였던 무언가
    weight_map = dijkstra(start, data_list, N, M, weight_map)
    print(min(weight_map[-1]))


# 다익스트라..였던 무언가
def dijkstra(start, data_list, N, M, weight_map):
    # 큐 / queue[i] = [현재까지 경비, [좌표], 이전 선택]
    queue = start
    # 순회
    while queue:
        # 현재 비용, 현재 좌표, 이전 방향
        now_weight, [now_x, now_y], now_dir = heapq.heappop(queue)
        # 이동 가능 위치 탐색
        for dir in [-1, 0, 1]:
            # 이전 방향이랑 같으면 패스
            if dir == now_dir:
                continue
            # 이동 위치
            next_x = now_x + 1
            next_y = now_y + dir
            # 이동 방향에 길이 있으면
            if 0<=next_y<M and 0<=next_x<N:
                # 큐에 추가
                heapq.heappush(queue, [now_weight+data_list[next_x][next_y], [next_x, next_y], dir])
                # 비용이 더 적으면 비용 맵 최신화
                if now_weight+data_list[next_x][next_y] < weight_map[next_x][next_y]:
                    weight_map[next_x][next_y] = now_weight+data_list[next_x][next_y]
    return weight_map


N, M = map(int, input().split())
data_list = [list(map(int, input().split())) for _ in range(N)]
solution(N, M, data_list)