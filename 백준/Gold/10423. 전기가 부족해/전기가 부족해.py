import sys

input = sys.stdin.readline


## Union-Find
# Find
def Find(group_list, n):
    # 자신이 그룹의 대표가 아니면
    if group_list[n] != n:
        # 재귀적으로 업데이트
        group_list[n] = Find(group_list, group_list[n])
    
    return group_list[n]


# Union
def Union(group_list, generator_group, n1, n2):
    # 그룹
    g1 = Find(group_list, n1)
    g2 = Find(group_list, n2)
    # 두 그룹이 같거나 두 그룹 모두에 발전기가 있으면
    if g1 == g2 or (g1 in generator_group.values() and g2 in generator_group.values()):
        # 병합하지 않음
        return False, group_list, generator_group

    # 두 그룹이 다르면 그룹이 작은쪽으로 병합
    if g1 < g2:
        group_list[g2] = g1
    
    else:
        group_list[g1] = g2
    
    # 발전기 그룹 갱신
    for key, value in generator_group.items():
        generator_group[key] = Find(group_list, value)

    return True, group_list, generator_group


def solution(N, M, K, generator, edges):
    # 엣지 정렬
    edges = sorted(edges, key=lambda x: x[-1])
    # 코스트 합
    cost = 0
    # 그룹 리스트
    group_list = list(range(N+1))
    # 발전기 그룹
    generator_group = {g : g for g in generator}
    # 엣지 순회하며 연결
    for u, v, w in edges:
        # 병합
        state, group_list, generator_group = Union(group_list, generator_group, u, v)
        # 병합에 성공하면
        if state:
            # 코스트 합
            cost += w

    print(cost)


# 입력
N, M, K = map(int, input().strip().split())
generator = list(map(int, input().strip().split()))
edges = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, K, generator, edges)