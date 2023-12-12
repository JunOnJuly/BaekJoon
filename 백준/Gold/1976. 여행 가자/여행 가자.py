from collections import deque


def solution(N, M, data_list, plan):
    # 루트 노드 리스트
    union_list = list(range(N+1))
    # 방문 리스트
    visited = [1 for _ in range(N+1)]
    visited[0] = 0
    visited[1] = 0
    # 큐
    queue = deque([1])
    # 루트 노드 정리
    while True:
        # 모든 노드를 방문했고 큐가 비면 끝
        if not any(visited) and not queue:
            break
        # 방문하지 않은 노드가 있고 큐가 비면
        elif not queue:
            # 방문하지 않은 노드 큐에 넣기
            for idx in range(len(visited)):
                if visited[idx]:
                    queue.append(idx)
                    visited[idx] = 0
                    break
        # 현재 노드
        now_node = queue.popleft()
        # 방문하지 않은 이어져 있는 노드를 순서대로 탐색
        for next_node in range(len(data_list[now_node-1])):
            if visited[next_node+1] and data_list[now_node-1][next_node]:
                # 부모 노드를 업데이트
                union_list[next_node+1] = now_node
                # 방문 목록 업데이트
                visited[next_node+1] = 0
                # 큐에 추가
                queue.append(next_node+1)
    # 루트 노드 병합
    for idx_1 in range(1, N+1):
        for idx_2 in range(idx_1+1, N+1):
            union_list = union(union_list, idx_1, idx_2)
    # 여행지들의 루트 노드가 모두 같으면 yes
    if len(set([union_list[node] for node in plan])) == 1:
        print('YES')
    else:
        print('NO')


# 루트 노드를 찾는 함수
def find(union_list, find_num):
    # 루트 노드의 경우
    if union_list[find_num] == find_num:
        return find_num
    # 아닐 경우 재귀적으로 탐색하며 할당
    union_list[find_num] = find(union_list, union_list[find_num])
    return union_list[find_num]


# 같은 루트 노드를 가진 노드를 병합
def union(union_list, find_num_1, find_num_2):
    # 루트 노드 탐색
    root_1 = find(union_list, find_num_1)
    root_2 = find(union_list, find_num_2)
    # 루트 노드 정리
    if root_1 == root_2:
        union_list[root_2] = root_1
    return union_list


N = int(input())
M = int(input())
data_list = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))
solution(N, M, data_list, plan)