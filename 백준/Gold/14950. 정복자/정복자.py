import sys

input = sys.stdin.readline


## Union-Find
# Find
def Find(group_list, node):
    # 그룹의 대표가 자신이 아니면
    if group_list[node] != node:
        # 재귀적으로 업데이트
        group_list[node] = Find(group_list, group_list[node])
    
    return group_list[node]


# Union
def Union(group_list, n1, n2):
    # 그룹
    g1 = Find(group_list, n1)
    g2 = Find(group_list, n2)
    # 두 그룹이 같으면
    if g1 == g2:
        # 병합하지 않음
        return False, group_list

    # 두 그룹이 다르면 작은 그룹으로 병합
    if g1 < g2:
        group_list[g2] = g1
    
    else:
        group_list[g1] = g2
    
    return True, group_list


def solution(N, M, t, edges):
    # 엣지 정렬
    edges = list(sorted(edges, key=lambda x: x[-1]))
    # 추가된 비용
    added_cost = 0
    # 총 코스트
    total_cost = 0
    # 그룹 리스트
    group_list = list(range(N+1))
    # 엣지 순회
    for A, B, C in edges:
        # 병합
        state, group_list = Union(group_list, A, B)
        # 병합 되었으면
        if state:
            # 코스트 더해주기
            total_cost += C + added_cost
            # 추가 코스트 갱신
            added_cost += t
    
    print(total_cost)


# 입력
N, M, t = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, t, edges)