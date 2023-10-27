def solution(N, field):
    # 최대 지역 수
    max_cnt = 0
    # 물의 수위
    max_water = max([max(row) for row in field])
    # 물의 수위를 변경해가며
    for water in range(max_water+1):
        # 지역 수
        cnt = 0
        # 방문 기록
        visited = [[1 for _ in range(N)] for __ in range(N)]
        # 수위 조절
        visited = water_fill(field, visited, water, N)
        while True:
            # 시작지점 찾기
            start = find_start(N, visited)
            # 시작지점이 있으면
            if start:
                cnt += 1
                visited[start[0]][start[1]] = 0
                # DFS
                visited = dfs(field, visited, start, N)
                continue
            else:
                # 최대 카운트 최신화
                if max_cnt < cnt:
                    max_cnt = cnt
                break
    return max_cnt
    
    
# 수위 조절하기
def water_fill(field, visited, water, N):
    for i in range(N):
        for j in range(N):
            # 지역이 수위보다 낮으면 방문 불가
            if field[i][j] <= water:
                visited[i][j] = 0
    return visited
    
    
# 시작지점 찾기
def find_start(N, visited):
    # 스택
    start = []
    # 순서대로 순회하며 시작점 찾기
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                start = [i, j]
                return start
    return start


# DFS
def dfs(field, visited, start, N):
    # 이동 가이드
    guide_x = [0, 1, 0, -1]
    guide_y = [1, 0, -1, 0]
    # 스택
    stack = [start]
    
    while True:
        # 중단조건
        if not stack:
            return visited
        # 현재 위치
        now = stack[-1]
        now_x = stack[-1][0]
        now_y = stack[-1][1]
        # 다음 위치
        for idx, (x, y) in enumerate(zip(guide_x, guide_y)):
            next_x = now_x + x
            next_y = now_y + y
            # 인덱스 범위 안에 있고 방문한 적이 없으면
            if (next_x >= 0 and next_x < N) and \
                (next_y >= 0 and next_y < N) and \
                (visited[next_x][next_y]):
                # 다음 경로에 추가
                stack.append([next_x, next_y])
                # 방문 기록
                visited[next_x][next_y] = 0
                break
            # 이동 가능 위치가 없으면
            elif idx == 3:
                stack.pop()

                
N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, field))