def solution(dirs):
    # 방향 매칭
    dir_dict = {"U": 0, "D": 1, "R": 2, "L": 3}
    # 이동 방향 매칭
    move_dict = {"U" : [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}
    # 방문 기록
    visited = [[[1, 1, 1, 1] for _ in range(-5, 6)] for __ in range(-5, 6)]
    # 위치
    idx = [0, 0]
    # 명령어 순회
    for order in dirs:
        # 인덱스 합
        next_idx = [idx[0] + move_dict[order][0], idx[1] + move_dict[order][1]]
        # 좌표계 내부면
        if (next_idx[0] >= -5 and next_idx[0] <= 5) and \
            (next_idx[1] >= -5 and next_idx[1] <= 5):
            # 기록
            if visited[idx[0] + 5][idx[1] + 5][dir_dict[order]] == 1:
                visited[idx[0] + 5][idx[1] + 5][dir_dict[order]] = -1 
            # 이동
            idx = next_idx
            # 반대 기록
            if dir_dict[order] % 2 and visited[idx[0] + 5][idx[1] + 5][dir_dict[order] - 1] == 1:
                visited[idx[0] + 5][idx[1] + 5][dir_dict[order] - 1] = 0
            elif not dir_dict[order] % 2 and visited[idx[0] + 5][idx[1] + 5][dir_dict[order] + 1] == 1:
                visited[idx[0] + 5][idx[1] + 5][dir_dict[order] + 1] = 0
    # 카운트
    cnt = 0
    for vstd in visited:
        for vs in vstd:
            cnt += vs.count(-1)
    return cnt
    