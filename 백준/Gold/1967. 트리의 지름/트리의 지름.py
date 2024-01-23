import heapq
import sys
input = sys.stdin.readline


def solution(n, data_list):
    # 다익스트라
    # 트리 / tree[i] = [[i 와 연결된 노드, 거리], ... ]
    tree = [[] for _ in range(n+1)]
    for parent, child, dir in data_list:
        tree[parent].append([child, dir])
        tree[child].append([parent, dir])
    # 루트에서 가장 먼 노드
    far_root_dir, far_root_node = dijkstra(1, tree, n)
    # 에서 가장 먼 노드
    far_far_dir, far_far_node = dijkstra(far_root_node, tree, n)
    # 출력
    print(far_far_dir)


# 다익스트라
def dijkstra(start, tree, n):
    # 큐
    queue = [[0, start]]
    # 시스템상 최대거리
    inf = float('INF')
    # 노드까지의 최단 거리 리스트
    min_dir_list = [inf for _ in range(n+1)]
    min_dir_list[start] = 0
    # 가장 긴 길이
    far_dir = 0
    # 가장 먼 노드
    far_node = 0
    # 순회
    while queue:
        # 현재 거리, 현재 노드
        now_dir, now_node = heapq.heappop(queue)
        # 현재 거리가 최단 거리보다 크면 패스
        if now_dir > min_dir_list[now_node]:
            continue
        # 자식 순회
        for next_node, dir in tree[now_node]:
            # 다음 거리
            next_dir = now_dir + dir
            # 다음 거리가 최단거리보다 짧으면
            if next_dir < min_dir_list[next_node]:
                heapq.heappush(queue, [next_dir, next_node])
                # 최단거리 리스트에 최신화
                min_dir_list[next_node] = next_dir
                # 가장 먼 노드의 거리보다 다음 거리가 길면 가장 먼 노드 최신화
                if far_dir < next_dir:
                    far_dir = next_dir
                    far_node = next_node
    return far_dir, far_node


n = int(input())
data_list = [list(map(int, input().strip().split())) for _ in range(n-1)]
solution(n, data_list)