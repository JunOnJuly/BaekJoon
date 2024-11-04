import sys

input = sys.stdin.readline


## Union-Find
# Union
def Union(group_list, n1, n2):
    # 각 그룹
    g1 = Find(group_list, n1)
    g2 = Find(group_list, n2)
    # 두 그룹이 같으면
    if g1 == g2:
        # 병합하지 않음
        return False, group_list
    
    # 두 그룹이 다르면
    # 작은 쪽으로 병합
    if g1 > g2:
        group_list[g1] = g2
    
    else:
        group_list[g2] = g1
    
    return True, group_list


# Find
def Find(group_list, n):
    # 자신이 그룹의 대표가 아니면
    if group_list[n] != n:
        # 재귀적으로 업데이트
        group_list[n] = Find(group_list, group_list[n])
    
    return group_list[n]


def solution(m, n, edges):
    # 엣지 정렬
    edges = sorted(edges, key=lambda x:x[-1])
    # 그룹 리스트
    group_list = list(range(m))
    # 절약할 수 있는 비용
    sub_cost = sum([z for x, y, z in edges])
    # 연결
    for x, y, z in edges:
        # 병합
        state, group_list = Union(group_list, x, y)
        # 병합됐으면
        if state:
            # 코스트 빼주기
            sub_cost -= z
    
    print(sub_cost)


# 입력
while True:
    m, n = map(int, input().strip().split())
    if not m:
        break

    edges = [list(map(int, input().strip().split())) for _ in range(n)]

    solution(m, n, edges)