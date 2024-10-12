import sys
from collections import deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


# 자식 노드의 수를 찾는 함수
def cal_child(tree, childs, node):
    # 자손의 수가 구해져 있지 않으면
    if childs[node] < 0:
        # 자식이 없으면 0
        if not tree[node]:
            childs[node] = 0
        
        # 자식이 있으면 자식들의 자손의 합에 자식의 수 더해주기
        else:
            childs[node] = sum([cal_child(tree, childs, child) + 1 for child in tree[node]])

    return childs[node]
    

def solution(N, R, Q, edges, querys):
    # 트리 / tree[i] = [연결된 노드들]
    tree = [[] for _ in range(N+1)]
    for s, e in edges:
        tree[s].append(e)
        tree[e].append(s)
    
    # 방문목록
    visited = [True for _ in range(N+1)]
    # 데크
    dq = deque([R])
    visited[R] = False
    # 순회
    while dq:
        # 현재 노드
        now_node = dq.popleft()
        # 자식 노드 리스트
        child_nodes = []
        # 연결된 노드 순회
        for node in tree[now_node]:
            # 방문하지 않았으면
            if visited[node]:
                # 방문 체크
                visited[node] = False
                # 데크에 추가
                dq.append(node)
                # 자식 노드 리스트에 추가
                child_nodes.append(node)
        
        # 트리 업데이트
        tree[now_node] = child_nodes

    # 자식의 수
    childs = [-1 for _ in range(N+1)]
    # 쿼리에 따른 답 출력
    for query in querys:
        print(cal_child(tree, childs, query) + 1)


# 입력
N, R, Q = map(int, input().strip().split())
edges = [list(map(int, input().strip().split())) for _ in range(N-1)]
querys = [int(input().strip()) for _ in range(Q)]

solution(N, R, Q, edges, querys)