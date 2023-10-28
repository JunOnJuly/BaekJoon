def solution(N, M, r, c, d, data_list):
    # 움직임 가이드
    guide_x = [0, 1, 0, -1, 0, 1, 0, -1, 0]
    guide_y = [-1, 0, 1, 0, -1, 0, 1, 0, -1]
    # DFS 쓸거임
    stack = [[r, c, d]]
    # 청소한 방의 수
    cnt = 0
    while True:
        # 현재 상태
        now = stack[-1]
        now_x = now[0]
        now_y = now[1]
        now_d = now[2]
        # 방을 청소
        if not data_list[now_x][now_y]:
            data_list[now_x][now_y] = -1
            cnt += 1
        # 방향에 따라 회전 시작점이 달라져야 하므로
        # 근데 회전 방향과 설정된 회전 방향이 반대라
        # -를 곱해서 인덱스 설정
        for idx, (x, y) in enumerate(zip(guide_x[-now_d-5: -now_d-1], guide_y[-now_d-5: -now_d-1])):
            # 다음 상태
            next_x = now_x + x
            next_y = now_y + y
            # 첫 방향에서 돌아가는 만큼
            next_d = (now_d+3-idx) % 4
            # 주변이 깨끗할 경우 후진 할 위치, 방향은 아직
            if idx == 1:
                back_dir = [next_x, next_y, 0]
            # 인덱스 안에 있고 청소되지 않은 칸일 때
            if (next_x >= 0 and next_x < N) and \
                (next_y >= 0 and next_y < M) and \
                (not data_list[next_x][next_y]):
                stack.append([next_x, next_y, next_d])
                break
            # 모든 방향이 청소되어 있거나 벽일 때
            elif idx == 3:
                # 후진 할 방향
                back_dir[2] = next_d
                # 후진할 수 없다면
                if data_list[back_dir[0]][back_dir[1]] == 1:
                    return cnt
                # 아니면
                else:
                    stack.append(back_dir)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
data_list = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, r, c, d, data_list))