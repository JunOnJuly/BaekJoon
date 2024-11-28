import sys

input = sys.stdin.readline


def solution(N, heights):
    # 수신탑 목록
    receive_list = [0]
    # 스택
    stack = [[0, heights[0]]]
    # 높이의 왼쪽부터 하나씩 추가
    for idx in range(1, len(heights)):
        # 현재 높이
        now_height = heights[idx]
        # 추가될 높이가 직전 높이보다 높으면 직전 높이는 소용 없음
        # 앞선 높이가 현재 높이보다 낮으면 모두 팝
        while stack and stack[-1][1] <= now_height:
            # 팝
            stack.pop()
        
        # 남은 탑이 없으면 0
        if not stack:
            receive_list.append(0)
        
        # 남은 탑이 있으면 마지막 탑 인덱스
        else:
            receive_list.append(stack[-1][0]+1)

        # 현재 높이 추가
        stack.append([idx, now_height])

    print(*receive_list)


# 입력
N = int(input().strip())
heights = list(map(int, input().strip().split()))

solution(N, heights)