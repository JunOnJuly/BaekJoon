import sys

input = sys.stdin.readline


# Union-Find
def Find(islands_group:list, island:int) -> int:
    # 그룹의 루트 노드가 아니면
    if islands_group[island] != island:
        islands_group[island] = Find(islands_group, islands_group[island])
    
    return islands_group[island]


def Union(island_group:list, i1:int, i2:int) -> tuple:
    # 그룹
    g1 = Find(island_group, i1)
    g2 = Find(island_group, i2)
    # 같은 그룹이면
    if g1 == g2:
        # 병합하지 않음
        return False, island_group

    # 작은 쪽으로 병합
    if g1 < g2:
        island_group[g2] = g1
    
    else:
        island_group[g1] = g2
    
    return True, island_group


# 연결할 수 있는 섬을 탐색하는 함수
def find_connectable(i:int, j:int, islands:list, islands_group:list, connects:list, N:int, M:int) -> list:
    # 현재 위치가 섬이라면
    if islands[i][j]:
        # 네 방향
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        # 네 방향 탐색
        for x, y in dirs:
            # 배수
            mul = 1
            # 탐색
            while True:
                # 현재 탐색 위치
                now_i = i + x*mul
                now_j = j + y*mul
                # 가장자리면 끝
                if now_i < 0 or now_i >= N or now_j < 0 or now_j >= M:
                    break
                    
                # 육지면
                elif islands[now_i][now_j]:
                    # 다른 섬이면
                    if islands_group[now_i*M + now_j] != islands_group[i*M + j]:
                        # 다리의 길이가 2 이상이면
                        if mul - 1 >= 2:
                            # 기록
                            connects.append([islands_group[now_i*M + now_j], islands_group[i*M + j], mul-1])
                        
                    break

                # 배수 + 1
                mul += 1
        
    return connects


def solution(N, M, islands):
    # 그룹 나누기
    islands_group = [M*i + j if islands[i][j] else -1 for i in range(N) for j in range(M)]
    # 순회
    for i in range(N):
        for j in range(M):
            # 해당 위치가 섬이면
            if islands[i][j]:
                # 정방향으로 탐색
                for x, y in [[1, 0], [0, 1]]:
                    # 탐색 위치
                    ii = i+x
                    jj = j+y
                    # 인덱스를 벗어나지 않고 섬이라면
                    if ii < N and jj < M and islands[ii][jj]:
                        # 병합
                        state, islands_group = Union(islands_group, M*i + j, M*ii + jj)
    
    # 정리
    for i in range(N):
        for j in range(M):
            if islands[i][j]:
                Find(islands_group, M*i + j)

    # 섬의 수
    island_cnt = len(set(islands_group)) - 1
    # 연결 가능 리스트
    connects = []
    # 모든 위치 순회
    for i in range(N):
        for j in range(M):
            # 연결 가능 여부 체크
            connects = find_connectable(i, j, islands, islands_group, connects, N, M)
    
    ## 크루스칼 알고리즘
    # 다리 길이순으로 정렬
    connects = sorted(connects, key=lambda x:x[-1])
    # 다리 길이
    total_length = 0
    # 다리의 수
    total_cnt = 0
    # 순서대로 병합
    for i1, i2, length in connects:
        state, islands_group = Union(islands_group, i1, i2)
        # 병합되었으면
        if state:
            # 길이 더해주기
            total_length += length
            # 수 더해주기
            total_cnt += 1
    
    print(total_length if total_cnt == island_cnt-1 else -1)


# 입력
N, M = map(int, input().strip().split())
islands = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, M, islands)