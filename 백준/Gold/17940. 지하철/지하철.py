import sys
from heapq import heappop as hpp
from heapq import heappush as hps

input = sys.stdin.readline


def solution(N, M, comps, edges):
    # 큐 / [환승 횟수, 노드, 거리]
    q = [[0, 0, 0]]
    # 최단거리
    min_dists = [[float('inf'), float('inf')] for _ in range(N)]
    min_dists[0] = [0, 0]
    # 순회
    while q:
        # 현재 환승횟수 / 노드 / 거리
        now_trans, now_node, now_dist = hpp(q)
        # 현재 환승횟수가 현재 노드의 최소 환승횟수보다 크면 패스
        if now_trans > min_dists[now_node][0]:
            continue

        # 현재 환승횟수가 현재 노드의 최소 환승횟수와 같지만 거리가 더 길면 패스
        if now_trans == min_dists[now_node][0] and now_dist > min_dists[now_node][1]:
            continue

        # 연결된 노드 탐색
        for next_node in range(N):
            # 이동할 수 있으면
            if edges[now_node][next_node]:
                # 거리
                dist = edges[now_node][next_node]
                # 다음 노드까지 거리
                next_dist = now_dist + dist
                # 다음 환승 횟수
                # 호선이 다르면
                if comps[now_node] != comps[next_node]:
                    next_trans = now_trans + 1 

                else:
                    next_trans = now_trans

                # 다음 환승횟수가 다음 노드의 최소 환승횟수보다 크면 패스
                if next_trans > min_dists[next_node][0]:
                    continue

                # 현재 환승횟수가 현재 노드의 최소 환승횟수와 같지만 거리가 더 길면 패스
                if next_trans == min_dists[next_node][0] and next_dist > min_dists[next_node][1]:
                    continue

                # 최단거리 갱신
                min_dists[next_node] = [next_trans, next_dist]
                # 큐에 추가
                hps(q, [next_trans, next_node, next_dist])
    
    print(*min_dists[M])


# 입력
N, M = map(int, input().strip().split())
comps = [int(input().strip()) for _ in range(N)]
edges = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, M, comps, edges)