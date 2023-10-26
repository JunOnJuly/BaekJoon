def solution(a, b, n, m, data_list):
    # 방문기록
    visited = [1 for _ in range(n+1)]
    visited[a] = 0
    # 트리
    tree = [[] for _ in range(n+1)]
    for parent, child in data_list:
        tree[parent].append(child)
        tree[child].append(parent)
    
    # DFS 쓸거임
    stack = [a]

    while True:
        # 경로가 없으면
        if not stack:
            return -1
        # b 에 도달했으면
        if stack[-1] == b:
            return len(stack)-1
        # 현재 노드
        now = stack[-1]
        for idx, node in enumerate(tree[now]):
            # 방문한 적 없으면
            if visited[node]:
                stack.append(node)
                visited[node] = 0
                break
            # 이동 가능 경로가 없으면
            elif idx == len(tree[now])-1:
                stack.pop()
                break


n = int(input())
a, b = map(int, input().split())
m = int(input())
data = [list(map(int, input().split())) for _ in range(m)]
print(solution(a, b, n, m, data))