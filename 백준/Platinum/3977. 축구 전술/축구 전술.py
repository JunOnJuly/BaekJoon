from collections import defaultdict, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def solution(V, E, edge_list):
    # 그래프 / graph[i] = [i 의 자식들]
    global graph
    graph = [[] for _ in range(V)]
    for parent, child in edge_list:
        graph[parent].append(child)
    # 스택
    global stack
    stack = []
    # scc 리스트
    global scc_list
    scc_list = [-1 for _ in range(V)]
    # 방문 기록
    global visited
    visited = [0 for _ in range(V)]
    # 방문 순서
    global visit_num
    visit_num = 0
    # 순서대로 노드 방문
    for node in range(0, V):
        # 방문한 적 없으면 방문
        if not visited[node]:
            tarjan(node)
    # scc 목록
    scc_keys = list(set(scc_list))
    # 외부 scc 진입차수 사전 / topol_list[i] = i 의 진입 차수
    topol_dict = defaultdict(int)
    for parent, child in edge_list:
        # 부모와 자식의 scc 가 다르면 진입차수 + 1
        if scc_list[parent] != scc_list[child]:
            topol_dict[scc_list[child]] += 1
    # 진입차수가 0 인 scc 리스트
    print_list = []
    count_manual = 0
    for num in scc_keys:
        if not topol_dict[num]:
            print_list.append(num)
    # 진입 차수가 0인 scc가 하나면 프린트
    if len(print_list) == 1:
        # scc 리스트 순회하며 프린트
        for node in range(0, V):
            if scc_list[node] == print_list[0]:
                print(node)
        print()
    # 아니면 confused
    else:
        print("Confused")
        print()


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
        elif scc_list[node] < 0:
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


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    edge_list = [list(map(int, input().split())) for _ in range(E)]
    if t < T-1:
        space = input()
    solution(V, E, edge_list)