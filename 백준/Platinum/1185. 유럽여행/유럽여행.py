import sys

input = sys.stdin.readline


# Union-Find
def Union(root_list, node_1, node_2):
    # 각 노드의 루트
    root_node_1 = Find(root_list, node_1)
    root_node_2 = Find(root_list, node_2)
    # 두 노드의 루트가 같으면
    if root_node_1 == root_node_2:
        # 병합하지 않고 루트 리스트 리턴
        return False, root_list
    
    # 두 노드의 루트가 다르면
    else:
        # 루트가 작은쪽으로 병합하고 루트리스트 리턴
        if root_node_1 < root_node_2:
            root_list[root_node_2] = root_list[root_node_1]
        else:
            root_list[root_node_1] = root_list[root_node_2]

        return True, root_list


def Find(root_list, node):
    # 자신의 루트가 자신이 아니라면
    if root_list[node] != node:
        # 거슬러 올라가며 루트 정렬
        root_list[node] = Find(root_list, root_list[node])
    
    return root_list[node]


def solution(N, P, node_costs, edge_costs):
    # 크루스칼 알고리즘 응용
    # 원래는 엣지의 비용만 생각하지만
    # 출발하는 국가 방문 비용 + 엣지 비용*2 + 도착하는 국가 방문 비용 고려
    # 계산시에 출발국가 방문 비용 + 엣지비용 + 도착국가 방문 비용 + 엣지비용이 필요하기 때문
    # 종합 비용
    total_costs = [[s, e, l*2 + node_costs[s] + node_costs[e]] for s, e, l in edge_costs]
    # 비용 순으로 정렬
    total_costs = sorted(total_costs, key=lambda x: x[-1])
    # 최소 엣지 비용
    min_edge_cost = 0
    # Union-Find 를 위한 루트 리스트
    root_list = list(range(N+1))
    # 종합 비용이 적은 순으로 엣지 순회
    for s, e, l in total_costs:
        # s 노드와 e 노드 사이에 순환이 없다면 연결
        state, root_list = Union(root_list, s, e)
        # 연결 되었으면
        if state:
            # 비용 더해주기
            min_edge_cost += l

    # 시작 국가는 처음에 한번 더 방문하므로 더해주기
    return min_edge_cost + min(node_costs)


# 입력
N, P = map(int, input().strip().split())
node_costs = [float('inf')] + [int(input().strip()) for _ in range(N)]
edge_costs = [list(map(int, input().strip().split())) for _ in range(P)]

print(solution(N, P, node_costs, edge_costs))