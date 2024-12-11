import sys
from collections import deque

input = sys.stdin.readline
      

def solution(V, E, edges):
    # 그래프
    graph = [[] for _ in range(V+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # 색
    colors = [0 for _ in range(V+1)]
    # 큐
    dq = deque([])
    # 순회
    while True:
        # 순회하지 않은 노드 큐에 넣기
        for c in range(1, len(colors)):
            if not colors[c]:
                dq.append([c, 1])
                colors[c] = 1
                break
        
        # 큐가 비어있으면
        if not dq:
            # 이분 그래프
            print('YES')
            return
        
        # BFS
        while dq:
            # 현재 노드 / 색 
            now_node, now_color = dq.popleft()
            # 이동 가능한 노드 순회
            for next_node in graph[now_node]:
                # 방문하지 않았으면
                if not colors[next_node]:
                    # 큐에 넣기
                    dq.append([next_node, -now_color])
                    # 방문 체크
                    colors[next_node] = -now_color
                
                # 방문 했으면
                else:
                    # 현재 노드의 색과 같은 색이면 이분 그래프가 아님
                    if colors[next_node] == now_color:
                        print('NO')
                        return


# 입력
K = int(input().strip())
for _ in range(K):
    V, E = map(int, input().strip().split())
    edges = [list(map(int, input().strip().split())) for _ in range(E)]
    
    solution(V, E, edges)