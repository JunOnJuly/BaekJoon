import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def solution(V, E, edge_list):
    # 그래프 / graph[i] = [i 의 자식들]
    global graph
    graph = [[] for _ in range(V+1)]
    for parent, child in edge_list:
        graph[parent].append(child)
    # 스택
    global stack
    stack = []
    # scc 리스트
    global scc_list
    scc_list = [0 for _ in range(V+1)]
    # 방문 기록
    global visited
    visited = [0 for _ in range(V+1)]
    # 방문 순서
    global visit_num
    visit_num = 0
    # 순서대로 노드 방문
    for node in range(1, V+1):
        # 방문한 적 없으면 방문
        if not visited[node]:
            tarjan(node)
    print(str(len(set(scc_list[1:]))))
    for i in range(1, len(scc_list)):
        target_scc = scc_list[i]
        if scc_list[i]:
            for j in range(i, len(scc_list)):
                if target_scc == scc_list[j]:
                    print(j, end=' ')
                    scc_list[j] = 0
                if j == len(scc_list)-1:
                    print(-1)


# 타잔 알고리즘
def tarjan(now_node):
    # 방문 순서 + 1
    global visit_num
    visit_num += 1
    # 자신이 순환 시작 노드라고 가정
    lowest_node = visit_num
    # 방문 순서 기록
    visited[now_node] = visit_num
    # 스택에 추가
    stack.append(now_node)
    # 자식 순회
    for node in graph[now_node]:
        # 아직 방문하지 않은 자식이면
        if not visited[node]:
            # 순환 찾기 / 순환 중 시작 노드 찾기
            lowest_node = min(lowest_node, tarjan(node))
        # 방문 했지만 scc 가 결정이 안된 노드면
        elif not scc_list[node]:
            # 순환 끝에 순환 시작 노드 찾음
            lowest_node = min(lowest_node, visited[node])
    # 자신이 순환 시작 노드면
    if lowest_node == visited[now_node]:
        # 스택에서 자신이 나올때 까지 팝하면서 scc 기록
        while True:
            # 마지막 노드
            last_node = stack.pop()
            # scc 기록
            scc_list[last_node] = now_node
            # 스택의 마지막이 자신이면 끝
            if last_node == now_node:
                break
    return lowest_node


V, E = map(int, input().split())
edge_list = [list(map(int, input().strip().split())) for _ in range(E)]
solution(V, E, edge_list)