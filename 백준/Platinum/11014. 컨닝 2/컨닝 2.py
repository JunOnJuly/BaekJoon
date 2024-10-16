import sys

input = sys.stdin.readline


# 이분매칭
def bimatch(idx, connectable, connected, visited):
    # 이미 방문했으면 패스
    if visited[idx]:
        return False
    
    # 방문 체크
    visited[idx] = True
    # 순회
    for node in connectable[idx]:
        # 매칭할 수 있거나 다른 노드와 매칭시킬 수 있으면
        if connected[node] < 0 or bimatch(connected[node], connectable, connected, visited):
            # 매칭
            connected[node] = idx
            return True
    
    return False


def solution(N, M, tables):
    ## 최소 버텍스 커버 문제
    # 해당 문제에서 버텍스 -> 커닝의 가능성
    # 모든 버텍스를 커버하면 커닝의 가능성이 있는 모든 위치를 탐색하는 것과 동일
    # 즉 모든 버텍스를 커버하고 남은 자리에 앉히면 됨
    ## 해당 문제는 홀수 / 짝수 의 열로 이분그래프로 나타낼 수 있음
    # -> 짝수열에 학생을 앉히면 모든 버텍스는 홀수열로 향하기 때문
    # 해당 문제가 이분그래프에서의 최소 버텍스 커버 문제라면 이분매칭으로 풀 수 있음
    # -> 쾨닉의 정리
    # 즉 짝수 / 홀수 열로 나눈 이분그래프에서
    # 이분매칭을 통해 최소 버텍스 커버의 답을 찾으면
    # 매칭된 자리는 앉을 수 없는 자리
    # 짝수 -> 홀수 로의 이분매칭이었다면 짝수열에는 모두 앉을 수 있으므로
    # 홀수 -> 짝수 로의 이분매칭이었다면 홀수열에는 모두 앉을 수 있으므로
    # 결국 전체 자리수 - 매칭 된 자리의 수 가 답이됨
    
    # 매칭될 수 있는 리스트(짝수 -> 홀수) 
    connectable = [[] for _ in range(((M+1)//2) * N)]
    # 매칭된 리스트(홀수 -> 짝수)
    connected = [-1 for _ in range((M//2) * N)]
    # 탐색 가이드 / [1, -1] 과 [1, 1] 은 상대가 나를 볼 수 있으므로 탐색
    search_guide = [[-1, -1], [0, -1], [1, -1], [-1, 1], [0, 1], [1, 1]]
    # 순회
    for n in range(N):
        # 짝수만 순회
        for m in range(0, M, 2):
            # 현재 위치가 앉을 수 있는 위치면
            if tables[n][m] == '.':
                # 현재 위치에서 앉을 수 없는 자리 탐색
                for i, j in search_guide:
                    # 탐색 인덱스
                    nn = n+i
                    nm = m+j
                    # 탐색 인덱스가 범위 내에 있고 앉을 수 있다면
                    if (nn >= 0 and nn < N) and (nm >= 0 and nm < M) and (tables[nn][nm] == '.'):
                        # 탐색 가능 리스트에 추가
                        # 짝수 / 홀수 인덱스를 압축해 연속된 인덱스로 표현
                        connectable[(m//2) * N + n].append((nm//2) * N + nn)

    # 순회
    for idx in range(len(connectable)):
        # 방문 목록
        visited = [False for _ in range(len(connectable))]
        # 이분매칭
        bimatch(idx, connectable, connected, visited)
    
    # 매칭된 수
    matched = sum([1 for c in connected if c >= 0])
    # 전체 자리수
    table_num = 0
    for row in tables:
        table_num += sum([1 for r in row if r=='.'])
    
    print(table_num - matched)


# 입력
C = int(input().strip())
for _ in range(C):
    N, M = map(int, input().strip().split())
    tables = [list(input().strip()) for _ in range(N)]
    
    solution(N, M, tables)