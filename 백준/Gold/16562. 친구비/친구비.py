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


def solution(N, M, K, friends, rels):
    # 그룹 리스트
    group_list = list(range(N+1))
    # 그룹 나누기
    for a, b in rels:
        state, group_list = Union(group_list, a, b)

    # 그룹 갱신
    for i in range(1, N+1):
        Find(group_list, i)
    
    # 각 그룹에 속한 인원 중 가장 친구비가 적은 가격
    pays = [float('inf') for _ in range(N+1)]
    for g in range(1, len(group_list)):
        # 그룹
        group = group_list[g]
        # 가격
        pay = friends[g-1]
        # 최소 가격 갱신
        pays[group] = min(pays[group], pay)
    
    # 최소비용
    min_pay = sum([pay for pay in pays if pay != float('inf')])
    # 모든 친구를 사귈 수 있으면
    if min_pay <= K:
        print(min_pay)
    
    else:
        print("Oh no")


# 입력
N, M, K = map(int, input().strip().split())
friends = list(map(int, input().strip().split()))
rels = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, K, friends, rels)