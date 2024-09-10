import sys

input = sys.stdin.readline


# 이분 매칭
def bimatch(idx):
    # 방문했으면 패스
    if visited[idx]:
        return False
    # 방문 체크
    visited[idx] = True

    # 연결될 수 있는 노드 체크
    for node in bi_graph[idx]:
        # 연결되지 않았거나
        # 연결된 노드와 연결된 노드가 다른 노드를 선택할 수 있으면
        if connected[node] < 0 or bimatch(connected[node]):
            # 연결
            connected[node] = idx
            return True    
    return False


def solution(n):
    # 결과
    result = 0
    # 연결 기록(열노드)
    global connected
    connected = [-1 for _ in range(n)]
    # 행노드 순회하며 이분매칭
    for idx in range(n):
        # 방문 기록(행노드)
        global visited
        visited = [False for _ in range(n)]
        if bimatch(idx):
            result += 1

    return result


# 입력
n, k =  map(int, input().strip().split())
bi_graph = [[] for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().strip().split())
    bi_graph[r-1].append(c-1)

print(solution(n))