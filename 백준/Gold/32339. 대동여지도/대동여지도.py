import sys

sys.setrecursionlimit(10000)
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


def solution(N, M, priority, edges):
    # 선호도
    priority = {p:i for i, p in enumerate(priority)}
    # 엣지 정렬
    edges = sorted(edges, key=lambda x:(x[2], priority[x[3]]))
    # 그룹 리스트
    group_list= list(range(N+1))
    # 도로 설치 비용
    cost = 0
    # 도로 상세
    roads = [[0, 0], [0, 0], [0, 0]]
    # 순회
    for u, v, w, k in edges:
        # 병합
        state, group_list = Union(group_list, u, v)
        # 병합되었으면
        if state:
            # 설치비용 더해주기
            cost += w
            # 도로 상세 갱신
            roads[k][0] += 1
            roads[k][1] += w
    
    print(cost)
    for road in roads:
        print(*road)
    

# 입력
N, M = map(int, input().strip().split())
priority = list(map(int, input().strip().split()))
edges = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, priority, edges)