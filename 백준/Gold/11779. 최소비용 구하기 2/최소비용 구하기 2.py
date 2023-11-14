import heapq

def solution(n, m, data_list, start_node, end_node):
    # 데이터 정리
    simple_data = [[] for _ in range(n+1)]
    for start, end, weight in data_list:
        simple_data[start].append([weight, end])
    # 문제 내에서의 최장길이
    inf = 100000001
    # start 에서 부터의 거리
    dist = [inf for _ in range(n+1)]
    # start 까지의 거리는 0
    dist[start_node] = 0
    # 힙큐
    hq = [[0, start_node, [start_node]]]
    # 최소 경로
    min_visited = []
    # 다익스트라
    while True:
        # 큐가 비면 끝
        if not hq:
            return dist[end_node], len(min_visited), min_visited
        # 현재까지의 가중치, 현재 노드, 방문 노드
        now_weight, now_node, visited = heapq.heappop(hq)
        # 가중치가 현재 최소 길이보다 크면 종료
        if now_weight > dist[now_node]:
            continue
        # 순회
        # 현재 노드에서 갈 수 있는 위치와 가중치
        for add_weight, next_node in simple_data[now_node]:
            # 다음 노드로 가져갈 가중치
            next_weight = now_weight + add_weight
            # 현재 다음 노드의 가중치와 비교 및 최신화
            if next_weight < dist[next_node]:
                dist[next_node] = next_weight
                # 누적 가중치, 다음 노드정보, 방문 노드를 힙큐에 담기
                heapq.heappush(hq, [next_weight, next_node, visited + [next_node]])
                if next_node == end_node:
                    min_visited = visited + [next_node]


n = int(input())
m = int(input())
data_list = [list(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())
min_value, visit_len, visit_list = solution(n, m, data_list, start, end)

print(min_value)
print(visit_len)
print(*visit_list)