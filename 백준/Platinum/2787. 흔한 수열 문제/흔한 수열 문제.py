import sys

input = sys.stdin.readline


# 이분매칭
def bimatch(idx, range_list, connected, visited, excluded_idxs):
    # 이미 방문한 노드면 탐색 안함
    if visited[idx]:
        return False
    # 방문 체크
    visited[idx] = True
    # 탐색 가능한 노드 탐색
    x, y = range_list[idx]
    for node in range(x, y+1):
        # 다른 노드에 꼭 포함되어야 하는 노드가 아니고
        # 연결할 수 있거나 연결된 노드를 다른 노드로 옮길 수 있다면
        if node not in excluded_idxs[idx] and \
            (not connected[node] or bimatch(connected[node], range_list, connected, visited, excluded_idxs)):
            # 연결
            connected[node] = idx
            return True
        
    return False


def solution(N, M, informs):
    # 인덱스당 될 수 있는 수의 최소 / 최대
    range_list = [[1, N] for _ in range(N+1)]
    # 인덱스당 들어갈 수 없는 수 리스트
    excluded_idxs = [[] for _ in range(N+1)]
    for i in range(M):
        c, x, y, v = informs[i]
        # 1 이면
        if c == 1:
            # 최댓값 갱신
            for j in range(x, y+1):
                range_list[j][1] = min(range_list[j][1], v)
    
        else:
            # 최솟값 갱신
            for j in range(x, y+1):
                range_list[j][0] = max(range_list[j][0], v)

        # 들어갈 수 없는 수 갱신
        for j in range(x):
            excluded_idxs[j].append(v)
        for j in range(y+1, N+1):
            excluded_idxs[j].append(v)

    # 배치된 수
    connected = [0 for _ in range(N+1)]
    # 순회
    for i in range(1, N+1):
        # 방문 목록
        visited = [False for _ in range(N+1)]
        # 이분매칭
        bimatch(i, range_list, connected, visited, excluded_idxs)

    # 수열
    nums = [0 for _ in range(N)]
    # 매칭
    for i in range(1, len(connected)):
        if connected[i] == 0:
            print(-1)
            return
        nums[connected[i]-1] = i

    print(*nums)

    
# 입력
N, M = map(int, input().strip().split())
informs = [list(map(int, input().strip().split())) for _ in range(M)]
solution(N, M, informs)