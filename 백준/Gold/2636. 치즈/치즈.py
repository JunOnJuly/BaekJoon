from collections import deque


def solution(N, M, data_list):
    # 맵을 탐색하며 녹을 위치 찾기 / 테두리는 빈칸이므로 해당 위치에서 BFS 하며 겉부분 탐색
    # 탐색 시작 지점
    melt_list = []
    for n in range(N):
        for m in range(M):
            # 테두리
            if not n or not m:
                melt_list.append([n, m])
    # 직전까지 남아있는 녹을 지점
    melt_num_list = []
    # 방문 지점
    visited = [[1 for _ in range(M)] for __ in range(N)]
    # 녹을 지점이 남아있는 동안
    while melt_list:
        # 녹을 지점
        melt_list, visited = bfs(data_list, melt_list, visited, N, M)
        # 녹을 지점 최신화
        melt_num_list.append(len(melt_list))
        # 녹을 지점 녹이기
        for melt_x, melt_y in melt_list:
            data_list[melt_x][melt_y] = 0
    print(len(melt_num_list)-1)
    print(melt_num_list[-2])


# BFS
def bfs(data_list, start_list, visited, N, M):  
    # 시작 지점에서 데이터 순회
    # 녹일 점
    melt_list = []
    # 이동 가이드
    move_guide = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # 큐
    queue = deque(start_list)
    # 순회
    while queue:
        # 현재 위치
        now_x, now_y = queue.popleft()
        # 방향 순회
        for x, y in move_guide:
            # 다음 인덱스
            next_x = now_x + x
            next_y = now_y + y
            # 인덱스 안에 있고 방문한적 없다면
            if (0<=next_x<N and 0<=next_y<M) and\
                visited[next_x][next_y]:
                # 방문 체크
                visited[next_x][next_y] = 0
                # 비어있는 공간이면
                if not data_list[next_x][next_y]:
                    # 큐에 추가
                    queue.append([next_x, next_y])
                # 치즈면
                else:
                    # 녹일 점 저장
                    melt_list.append([next_x, next_y])
    return melt_list, visited


N, M = map(int, input().split())
data_list = [list(map(int, input().split())) for _ in range(N)]
solution(N, M, data_list)