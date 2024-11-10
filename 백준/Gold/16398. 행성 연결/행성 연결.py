import sys

input = sys.stdin.readline


# union-find
def Union(group_list, n1, n2):
    # 그룹
    g1 = Find(group_list, n1)
    g2 = Find(group_list, n2)
    # 두 그룹이 같으면
    if g1 == g2:
        # 병합하지 않음
        return False, group_list
    
    # 다르면 그룹이 작은쪽으로 병합
    if g1 > g2:
        group_list[g1] = g2
    
    else:
        group_list[g2] = g1
    
    return True, group_list


def Find(group_list, n):
    # 자신이 그룹의 대표가 아니면
    if group_list[n] != n:
        # 재귀적으로 업데이트
        group_list[n] = Find(group_list, group_list[n])
    
    return group_list[n]


def solution(N, costs):
    # 코스트별로 정렬
    edges = []
    for i in range(N-1):
        for j in range(i+1, N):
            edges.append([i+1, j+1, costs[i][j]])

    edges = sorted(edges, key=lambda x: x[-1])
    # 코스트 합
    cost_sum = 0
    # 그룹
    group_list = list(range(N+1))
    # 크루스칼
    for s, e, c in edges:
        # 병합
        state, group_list = Union(group_list, s, e)
        # 병합되었으면 코스트 더해주기
        if state:
            cost_sum += c
    
    print(cost_sum)


# 입력
N = int(input().strip())
costs = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, costs)