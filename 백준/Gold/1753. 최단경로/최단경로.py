import heapq


def solution(V, E, K, data_list):
    # data_list 정리
    simple_data = [[] for _ in range(V+1)]
    for start, end, weight in data_list:
        simple_data[start].append([end, weight])
    # 다익스트라 쓸거
    # 시스템상 최댓값
    inf = 200001
    # 가중치
    dist = [inf for _ in range(V+1)]
    dist[K] = 0
    # 힙큐에 부시
    hq = []
    # 시작이 K 인 데이터 순회
    for end, weight in simple_data[K]:
        if dist[end] > weight:
            heapq.heappush(hq, [weight, end])
            dist[end] = weight

    # 다익스트라
    while True:
        # 큐가 비면 끝
        if not hq:
            break
        # 가중치와 현재 노드
        now_weight, now_node = heapq.heappop(hq)
        # 가중치가 다음 노드의 가중치보다 크면 패스
        for next_node, next_weight in simple_data[now_node]:
            if now_weight > dist[next_node]:
                continue
            # 가중치의 합
            weight_sum = next_weight + now_weight
            # 기존 가중치와 비교
            if weight_sum < dist[next_node]:
                dist[next_node] = weight_sum
                # 힙큐에 푸시
                heapq.heappush(hq, [weight_sum, next_node])


    for weight in dist[1:]:
        if weight == inf:
            print("INF")
        else:
            print(weight)


V, E = map(int, input().split())
K = int(input())
data_list = [list(map(int, input().split())) for _ in range(E)]
solution(V, E, K, data_list)