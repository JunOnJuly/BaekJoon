import heapq


def solution(N, data_list):
    # 다익스트라 사용해보자
    # 그래프 정리 / graph[i] = [i와 연결된 노드들]
    graph = [[] for _ in range(N+1)]
    for data in data_list:
        graph[data[0]].append(data[1])
        graph[data[1]].append(data[0])
    # 점수 리스트
    score_list = [0 for _ in range(N+1)]
    # 다익스트라
    for idx in range(1, N+1):
        # 점수 리스트에 추가
        score_list[idx] = dijkstra(idx, graph, N)
    # 최저 점수
    min_score = min(score_list[1:])
    print(f'{min_score} {score_list.count(min_score)}')
    for idx in range(len(score_list)):
        if score_list[idx] == min_score:
            print(idx, end=' ')


# 다익스트라
def dijkstra(start, graph, N):
    # 시스템상 최단거리
    inf = float("INF")
    # 최단거리 리스트
    dist_list = [inf]*(N+1)
    # 시작 위치 최단거리 0
    dist_list[start] = 0
    # 큐
    queue = [[0, start]]
    # 순회
    while queue:
        # 현재 거리, 현재 노드
        now_dist, now_node = heapq.heappop(queue)
        # 현재 거리가 최단거리보다 길면 패스
        if now_dist > dist_list[now_node]:
            continue
        # 연결된 노드 순회
        for node in graph[now_node]:
            # 다음 노드로의 거리가 다음 노드까지의 최단거리보다 길면 패스
            if now_dist+1 > dist_list[node]:
                continue
            # 최단거리 최신화
            dist_list[node] = now_dist+1
            # 큐에 추가
            queue.append([now_dist+1, node])
    return max([num if num != inf else 0 for num in dist_list])


N = int(input())
data_list = []
while True:
    data = input()
    if data != '-1 -1':
        data_list.append(list(map(int, data.split())))
    else:
        break
solution(N, data_list)