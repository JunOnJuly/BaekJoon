from collections import deque

def solution(N, data_list):
    # 임시 트리
    # 인덱스 맞추기 위해 + 1
    temp_tree = [[] for _ in range(N+1)]

    # 우선 데이터를 트리에 정리
    for data in data_list:
        temp_tree[data[0]].append(data[1])
        temp_tree[data[1]].append(data[0])

    # 트리에 있는 데이터를 정리
    # i 번째 노드의 상위노드가 데이터
    tree = [[] for _ in range(N+1)]
    # 순회 리스트
    visited = [1 for _ in range(N+1)]
    # 데크 사용
    node_list = deque([1])
    while True:
        if not node_list:
            break
        # 현재 노드
        now_node = node_list.popleft()
        visited[now_node] = 0
        # 연결된 노드
        for temp_node in temp_tree[now_node]:
            # 방문한 적이 있다면 트리에 추가
            # 상위에서부터 내려가기 때문에 방문했다면 상위노드임
            # 그러므로 상위노드에 추가함
            if visited[temp_node]:
                tree[temp_node].append(now_node)
                # 큐에 삽입
                node_list.append(temp_node)

    for num in tree:
        if num:
            print(*num)

N = int(input())
data_list = [list(map(int, input().split())) for _ in range(N-1)]
solution(N, data_list)