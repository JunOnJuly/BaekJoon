import sys
from collections import deque

input = sys.stdin.readline


def solution(T, cogs, k, rotates):
    # 톱니바퀴 데크로 치환
    cogs = list(map(deque, cogs))
    # 회전 쿼리 순회
    for idx, query in rotates:
        # 톱니 번호 치환
        idx = idx - 1
        ## 시작 위치에서 양쪽으로 어디까지 회전하는지 체크
        # 회전할 톱니
        rotate_cogs = deque([[idx, query]])
        # 왼쪽 / 오른쪽
        l = max(0, idx-1)
        r = min(T-1, idx+1)
        # 순회
        while True:
            # 시작할 때 회전할 톱니의 수
            start_rotates = len(rotate_cogs)
            # 가장 왼쪽 톱니
            left_cog = rotate_cogs[0]
            # 가장 오른쪽 톱니
            right_cog = rotate_cogs[-1]
            # 왼쪽 톱니가 돌 수 있는 톱니면
            if l < left_cog[0] and cogs[l][2] != cogs[left_cog[0]][6]:
                # 회전할 톱니에 추가
                rotate_cogs.appendleft([l, -left_cog[1]])
                l = max(0, l-1)
            
            # 왼쪽 톱니가 돌 수 있는 톱니면
            if r > right_cog[0] and cogs[r][6] != cogs[right_cog[0]][2]:
                # 회전할 톱니에 추가
                rotate_cogs.append([r, -right_cog[1]])
                r = min(T-1, r+1)

            # 끝날 때 회전할 톱니의 수
            end_rotates = len(rotate_cogs)
            # 양쪽 톱니가 돌 수 없으면
            if start_rotates == end_rotates:
                # 끝
                break
        
        # 톱니 회전
        while rotate_cogs:
            # 순서, 쿼리
            idx, query = rotate_cogs.popleft()
            # 회전
            cogs[idx].rotate(query)

    print(sum([cogs[i][0] for i in range(T)]))


# 입력
T = int(input().strip())
cogs = [list(map(int, list(input().strip()))) for _ in range(T)]
k = int(input().strip())
rotates = [list(map(int, input().strip().split())) for _ in range(k)]

solution(T, cogs, k, rotates)