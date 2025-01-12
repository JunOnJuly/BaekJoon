import sys
import heapq as hq
from collections import deque

input = sys.stdin.readline


def solution(N, K):
    # 최대 인덱스
    max_idx = 150000
    # 최소 도달 시간
    min_times = [float('inf') for _ in range(max_idx+1)]
    # 직전 위치
    before_idx = [-1 for _ in range(max_idx+1)]
    min_times[N] = 0
    # 큐 / [시간, 위치]
    q = [[0, N]]
    # 순회
    while True:
        # 현재 시간 / 위치
        now_time, now_idx = hq.heappop(q)
        # 현재 위치가 동생의 위치면
        if now_idx == K:
            # 순회 중지
            break

        # 현재 시간이 현재 위치에서의 최단 시간보다 길면 패스
        if now_time > min_times[now_idx]:
            continue

        # 현재 위치가 동생의 위치보다 작으면
        if now_idx < K:
            # 범위를 넘어가지 않는다면 더하기
            if now_idx + 1 <= max_idx and now_time+1 < min_times[now_idx+1]:
                hq.heappush(q, [now_time+1, now_idx+1])
                # 최소 시간 갱신
                min_times[now_idx+1] = now_time+1
                # 직전 위치 갱신
                before_idx[now_idx+1] = now_idx

            # 범위를 넘어가지 않으면 곱하기
            if now_idx * 2 <= max_idx and now_time+1 < min_times[now_idx*2]:
                hq.heappush(q, [now_time+1, now_idx*2])
                # 최소 시간 갱신
                min_times[now_idx*2] = now_time+1
                # 직전 위치 갱신
                before_idx[now_idx*2] = now_idx

        # 현재 위치가 동생의 위치보다 크면 빼기만 넣어줌
        # 물론 범위를 넘어가지 않는다면
        if now_idx - 1 >= 0 and now_time+1 < min_times[now_idx-1]:
            hq.heappush(q, [now_time+1, now_idx-1])
            # 최소 시간 갱신
            min_times[now_idx-1] = now_time+1
            # 직전 위치 갱신
            before_idx[now_idx-1] = now_idx

    ## 역추적
    # 경로
    route = deque([K])
    # 순회
    while route[0] != N:
        # 경로에 추가
        route.appendleft(before_idx[route[0]])

    print(min_times[K])
    print(*route)


# 입력
N, K = map(int, input().strip().split())

solution(N, K)