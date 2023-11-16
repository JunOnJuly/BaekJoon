import heapq

def solution(N, M, data_list):
    # 트리
    tree = [[] for _ in range(N+1)]
    for data in data_list:
        tree[data[0]].append(data[1])
        tree[data[1]].append(data[0])
    
    # 케비 베이컨 리스트
    kb_list = []
    # 모든 사람을 시작점으로 다익스트라
    for user in range(1, N+1):
        kb_list.append(dijkstra(user, tree, N))
    # 가장 작은 사람 출력
    return kb_list.index(min(kb_list))+1


def dijkstra(start, tree, N):
    # 시스템상 최대 수
    inf = 5000
    # 최단거리 리스트
    dist_list = [5000 for _ in range(N+1)]
    dist_list[start] = 0
    # 큐
    hq = [[0, start]]
    # 순회
    while True:
        # 큐가 비면 끝
        if not hq:
            return sum(dist_list[1:])
        # 누적거리, 현재 노드
        dist, now_node = heapq.heappop(hq)
        # 누적거리가 현재 노드의 최소거리보다 길면 패스
        if dist > dist_list[now_node]:
            continue
        # 다음 노드에서의 누적거리
        next_dist = dist + 1
        # 이동 가능한 노드 순회
        for next_node in tree[now_node]:
            # 다음 누적거리와 다음 최소거리 비교
            if dist_list[next_node] > next_dist:
                dist_list[next_node] = next_dist
                # 큐에 푸시
                heapq.heappush(hq, [next_dist, next_node])


N, M = map(int, input().split())
data_list = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, data_list))