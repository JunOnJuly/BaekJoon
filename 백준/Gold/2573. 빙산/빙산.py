import copy

def solution(N, M, field):
    # 소요 시간
    year = 0
    while True:
        # 덩어리 수
        cnt = 0
        # 방문 기록
        visited = [[1 if field[i][j] else 0 for j in range(M)] for i in range(N)]
        while True:
            # 시작 지점을 찾음
            start = find_start(N, M, field, visited)
            # 시작 지점이 있으면
            if start:
                cnt += 1
                # 덩어리가 둘 이상이면
                if cnt >= 2:
                    return year
                
                visited[start[0]][start[1]] = 0
                # dfs 하면서 동시에 녹임
                field, visited = dfs(N, M, field, visited, start)
                
            # 시작 지점이 없는데 덩어리도 없으면
            elif cnt == 0:
                return 0
            # 나머지
            else:
                year += 1
                break
        

def find_start(N, M, field, visited):
    # 순서대로 돌면서 시작지점 찾기
    start = []
    for i in range(N):
        for j in range(M):
            if field[i][j] and \
                visited[i][j]:
                start = [i, j]
                return start
    return start



def dfs(N, M, field, visited, start):
    # 이동 가이드
    x_guide = [0, 1, 0, -1]
    y_guide = [1, 0, -1, 0]
    # 스택
    stack = [start]
    # 참고용 필드 복사
    field_copy = copy.deepcopy(field)
    # 시작 지점 얼음 녹이기
    field[stack[-1][0]][stack[-1][1]] -= melt_ice(field_copy, stack[-1][0], stack[-1][1], x_guide, y_guide, N, M)
    if field[stack[-1][0]][stack[-1][1]] < 0:
        field[stack[-1][0]][stack[-1][1]] = 0
    while True:
        # 중단 조건
        if not stack:
            return field, visited
        # 현재 위치
        now = stack[-1]
        now_x = now[0]
        now_y = now[1]
        # 다음 위치
        for idx, (x, y) in enumerate(zip(x_guide, y_guide)):
            next_x = now_x + x
            next_y = now_y + y
            # 인덱스 안에 포함되고 방문하지 않았다면
            if (next_x >=0 and next_x < N) and \
                (next_y >= 0 and next_y < M) and \
                (field[next_x][next_y]) and \
                (visited[next_x][next_y]):
                # 다음 경로에 추가
                stack.append([next_x, next_y])
                # 방문 기록
                visited[next_x][next_y] = 0
                # 얼음 녹이기
                field[next_x][next_y] -= melt_ice(field_copy, next_x, next_y, x_guide, y_guide, N, M)
                # 0 보다 작으면
                if field[next_x][next_y] < 0:
                    field[next_x][next_y] = 0
                break
            # 가능 경로가 없으면
            elif idx == 3:
                stack.pop()


def melt_ice(field, now_x, now_y, x_guide, y_guide, N, M):
    # 녹일 횟수
    melt_count = 0
    for x, y in zip(x_guide, y_guide):
        next_x = now_x + x
        next_y = now_y + y
        if (next_x >= 0 and next_x < N) and \
            (next_y >= 0 and next_y < M) and \
            (not field[next_x][next_y]):
            melt_count += 1
    return melt_count

N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, field))