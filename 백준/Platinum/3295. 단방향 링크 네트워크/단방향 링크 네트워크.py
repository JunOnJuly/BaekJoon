import sys

input = sys.stdin.readline


# 이분매칭
def bimatch(idx, connectable, connected, visited):
    # 이미 방문한 노드면 탐색 안함
    if visited[idx]:
        return False
    # 방문 체크
    visited[idx] = True
    # 탐색 가능한 노드 탐색
    for node in connectable[idx]:
        # 연결할 수 있거나 연결된 노드를 다른 노드로 옮길 수 있다면
        if connected[node] < 0 or bimatch(connected[node], connectable, connected, visited):
            # 연결
            connected[node] = idx
            
            return True
        
    return False


def solution(n, m, data_list):
    # 선형 배열 -> 엣지의 수 : 노드 수 - 1
    # 링 -> 엣지의 수 : 노드 수
    # 결국 연결된 노드의 수가 가치
    # -> 가장 노드를 많이 연결할 수 있는 경우를 찾아라
    # -> 링 / 선형 배열은 컴퓨터 끼리의 1 대 1 구조임
    # 1->2 / 2->3 / 3->4 .. 등등
    # 양방향 노드이거나 한 노드에 두개의 엣지가 연결되는 경우는 없음
    # 결국 각 노드끼리 가장 많이 연결시킬 수 있는 경우를 찾으라는 얘기
    # -> 이분매칭
    # 탐색 가능한 노드 정리
    connectable = [[] for _ in range(n)]
    for o, i in data_list:
        connectable[o].append(i)
    # 연결된 노드
    connected = [-1 for _ in range(n)]
    # 시작 노드 순회
    for idx in range(n):
        # 방문 목록
        visited = [False for _ in range(n)]
        # 이분 매칭
        bimatch(idx, connectable, connected, visited)
    
    print(sum([1 for c in connected if c >= 0]))
    

# 입력
T = int(input().strip())
for t in range(T):
    n, m = map(int, input().strip().split())
    data_list = [list(map(int, input().strip().split())) for _ in range(m)]
    solution(n, m, data_list)