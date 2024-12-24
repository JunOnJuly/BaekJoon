import sys

input = sys.stdin.readline


## Union-Find

# Find
def Find(group_list, node):
    # 루트 노드가 아니면
    if group_list[node] != node:
        group_list[node] = Find(group_list, group_list[node])
    
    return group_list[node]


# Union
def Union(group_list, n1, n2):
    # 그룹
    g1 = Find(group_list, n1)
    g2 = Find(group_list, n2)
    # 같은 그룹이면
    if g1 == g2:
        # 병합하지 않음
        return False, group_list

    # 작은 쪽으로 병합
    if g1 < g2:
        group_list[g2] = g1
    
    else:
        group_list[g1] = g2

    return True, group_list


def solution(N, Ws, Es):
    # 최소비용
    min_cost = 0
    # 그룹
    group_list = list(range(N+1))
    # 엣지 정리
    Es = [[i, j, Es[i][j]] for i in range(N) for j in range(N) if i < j]
    # 우물을 파는 비용을 가상의 논에 연결하는 셈 치자
    for i in range(N):
        Es.append([i, N, Ws[i]])
    
    # 정렬
    Es.sort(key=lambda x:x[-1])
    # 순회하며 병합
    for a, b, c in Es:
        state, group_list = Union(group_list, a, b)
        # 병합 되었으면
        if state:
            # 최소비용 추가
            min_cost += c
    
    print(min_cost)


# 입력
N = int(input().strip())
Ws = [int(input().strip()) for _ in range(N)]
Es = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, Ws, Es)