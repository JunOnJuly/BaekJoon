import sys

input = sys.stdin.readline


## Union-Find

# Find
def Find(group_list, node):
    # 자신이 그룹의 대표가 아니면
    if group_list[node] != node:
        # 재귀적으로 재탐색
        group_list[node] = Find(group_list, group_list[node])
    
    return group_list[node]


# Union
def Union(group_list, n1, n2):
    # 그룹
    g1 = Find(group_list, n1)
    g2 = Find(group_list, n2)
    # 그룹이 같으면
    if g1 == g2:
        # 병합하지 않음
        return False, group_list

    # 그룹이 작은 쪽으로 병합
    if g1 < g2:
        group_list[g2] = g1
    
    else:
        group_list[g1] = g2
    
    return True, group_list


def solution(N, M, p, q, edges):
    # 엣지 정렬
    edges = sorted(edges, key=lambda x:x[-1])
    # 그룹 리스트
    group_list = list(range(N+1))
    # 순회
    for u, v, w in edges:
        # 병합
        state, group_list = Union(group_list, u, v)
        # 병합 되었으면
        if state:
            # u, v 가 p, q 인지 확인
            if u in [p, q] and v in [p, q]:
                print('YES')
                return
    
    print('NO')
    return


# 입력
T = int(input().strip())
for _ in range(T):
    N, M, p, q = map(int, input().strip().split())
    edges = [list(map(int, input().strip().split())) for _ in range(M)]

    solution(N, M, p, q, edges)