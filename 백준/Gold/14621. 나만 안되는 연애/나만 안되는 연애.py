import sys

input = sys.stdin.readline


## Union-Find
# Union
def Union(group_list, node1, node2):
    # 그룹
    g1 = Find(group_list, node1)
    g2 = Find(group_list, node2)
    # 같은 그룹이면
    if g1 == g2:
        # 변합하지 않음
        return False, group_list

    # 다른 그룹이면 작은 그룹으로 병합
    if g1 > g2:
        group_list[g1] = g2
    
    else:
        group_list[g2] = g1
    
    return True, group_list


# Find
def Find(group_list, node):
    # 그룹의 대표가 아니면
    if group_list[node] != node:
        # 재귀적으로 업데이트
        group_list[node] = Find(group_list, group_list[node])
    
    return group_list[node]


def solution(N, M, S, edges):
    # 경로 길이
    dist_sum = 0
    # 경로 개수
    dist_cnt = 0
    # 엣지 정렬
    edges = sorted(edges, key=lambda x:x[-1])
    # 그룹 리스트
    group_list = list(range(N+1))
    # 순회
    for u, v, d in edges:
        # 모든 경로가 연결되었으면 끝
        if dist_cnt >= N-1:
            break

        # 두 노드의 성별이 다르면
        if S[u-1] != S[v-1]:
            # 병합
            state, group_list = Union(group_list, u, v)
            # 연결했으면 경로 업데이트
            if state:
                dist_sum += d
                dist_cnt += 1
            
    # 모든 학교가 연결되지 않았으면
    if dist_cnt < N-1:
        print(-1)
    
    else:
        print(dist_sum)


# 입력
N, M = map(int, input().strip().split())
S = input().strip().split()
edges = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, S, edges)