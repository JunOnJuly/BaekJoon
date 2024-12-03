import sys

input = sys.stdin.readline


# Union-Find
# Union
def Union(group_list, n1, n2):
    # 그룹
    g1 = Find(group_list, n1)
    g2 = Find(group_list, n2)
    # 그룹이 같으면
    if g1 == g2:
        # 병합하지 않음
        return False, group_list

    # 그룹이 작은쪽으로 병합
    if g1 < g2:
        group_list[g2] = g1
    
    else:
        group_list[g1] = g2
    
    return True, group_list


# Find
def Find(group_list, node):
    # 자신의 그룹 찾기
    if group_list[node] != node:
        # 재귀적으로 업데이트
        group_list[node] = Find(group_list, group_list[node])

    return group_list[node]


def solution(N, M, S, E, edges):
    # 엣지 내림차순 정렬
    edges = sorted(edges, key=lambda x: x[-1], reverse=True)
    # 그룹 리스트
    group_list = list(range(N+1))
    # S 와 E 의 그룹이 같을 때 까지 병합
    for A, B, C in edges:
        # 병합
        state, group_list = Union(group_list, A, B)
        # 병합 되었으면
        if state:
            # S 와 E 의 그룹이 같으면
            if Find(group_list, S) == Find(group_list, E):
                # 현재 코스트
                print(C)

                return


# 입력
N, M = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(M)]
S, E = map(int, input().strip().split())

solution(N, M, S, E, edges)