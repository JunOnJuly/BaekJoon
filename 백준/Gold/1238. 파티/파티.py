import heapq

def solution(N, M, X, data_list):
    # 데이터 정리
    clean_data = [[] for _ in range(N+1)]
    # 방향을 바꾼 데이터
    reversed_data = [[] for _ in range(N+1)]
    for start, end, dist in data_list:
        clean_data[start].append([dist, end])
        reversed_data[end].append([dist, start])
    # 파티 지점에서 다른 지점까지의 거리
    return_list = dijkstra(X, clean_data, N)
    # 방향을 바꾼 데이터로 구하면 다른 지점에서 파티장소로 오는 거리
    to_list = dijkstra(X, reversed_data, N)
    # 가장 긴 거리 출력
    max_dist = max([return_list[n]+to_list[n] for n in range(1, N+1)])
    return max_dist


def dijkstra(start, clean_data, N):
    # 문제상 최댓값
    inf = 100000
    # 거리
    dist_list = [inf for _ in range(N+1)]
    dist_list[start] = 0
    # 큐
    hq = [[0, start]]
    while True:
        # 큐가 비면 끝
        if not hq:
            return dist_list
        # 누적 거리, 현재 노드
        dist, now_node = heapq.heappop(hq)
        # 누적 거리가 최소 거리보다 길면 패스
        if dist > dist_list[now_node]:
            continue
        # 이동 가능 거리 탐색
        for add_dist, next_node in clean_data[now_node]:
            # 다음 누적 거리
            next_dist = dist + add_dist
            # 저장된 최소거리보다 누적거리가 더 짧으면 최신화
            if next_dist < dist_list[next_node]:
                dist_list[next_node] = next_dist
                # 큐에 추가
                heapq.heappush(hq, [next_dist, next_node])


N, M, X = map(int, input().split())
data_list = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, X, data_list))