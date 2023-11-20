from collections import deque
from itertools import combinations
import copy

def solution(N, M, data_list):
    # 벽을 배기할 위치를 찾음
    wall_list = find_walls(N, M, data_list)
    # 최대 카운트
    max_count = 0
    # 벽 리스트를 순회하며 벽 배치
    for wall in wall_list:
        set_map = set_walls(wall, data_list)
        # 카운트
        cnt = bfs(N, M, set_map)
        # 최대치 최신화
        if cnt > max_count:
            max_count = cnt
    return max_count


# 벽을 배치하는 함수
def set_walls(wall, data_list):
    # 맵 카피
    maps = copy.deepcopy(data_list)
    # 벽을 순회하며 벽 배치
    for wall_idx in wall:
        maps[wall_idx[0]][wall_idx[1]] = 1
    return maps


# 벽을 배치할 위치를 찾는 함수
# combinations 활용
def find_walls(N, M, data_list):
    # 우선 블록을 설치할 인덱스를 1차원으로 펼쳐서 구함
    wall_idx_flat = list(combinations(list(range(N*M)), 3))
    # 2 차원 인덱스로 정리
    wall_idx_2d = []
    for wall_idx in wall_idx_flat:
        # 추가할 리스트
        temp_list = []
        # 해당 위치가 비어있으면 리스트에 추가
        for wall in wall_idx:
            if data_list[wall//M][wall%M]:
                break
            else:
                temp_list.append([wall//M, wall%M])
        # 리스트가 3개면 인덱스 리스트에 추가
        if len(temp_list) == 3:
            wall_idx_2d.append(temp_list)
    return wall_idx_2d


# 맵을 탐색해 안전구역을 검색하는 함수
# BFS
def bfs(N, M, data_list):
    # 큐
    queue = deque([])
    # 시작 지점 정하기
    for i in range(N):
        for j in range(M):
            if data_list[i][j] == 2:
                queue.append([i, j])
    # 탐색 방향 가이드
    move_guide_x = [0, 1, 0, -1]
    move_guide_y = [1, 0, -1, 0]
    # 탐색 시작
    while True:
        # 큐가 비면 비어있는 공간 카운팅
        if not queue:
            # 카운트
            cnt = 0
            for i in range(N):
                for j in range(M):
                    if data_list[i][j] == 0:
                        cnt += 1
            return cnt
        # 현재 인덱스
        now_x, now_y = queue.popleft()
        # 네 방향 탐색
        for x, y in zip(move_guide_x, move_guide_y):
            # 다음 인덱스 후보
            next_x = now_x + x
            next_y = now_y + y
            # 인덱스를 벗어나지 않는지, 비어있는 공간인지
            if (next_x >= 0 and next_x < N) and \
                (next_y >= 0 and next_y < M) and \
                (not data_list[next_x][next_y]):
                # 감염
                data_list[next_x][next_y] = 2
                # 큐에 삽입
                queue.append([next_x, next_y])


N, M = map(int, input().split())
data_list = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, data_list))