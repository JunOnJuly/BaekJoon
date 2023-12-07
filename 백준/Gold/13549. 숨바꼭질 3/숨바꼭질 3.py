import heapq


def solution(N, K):
    # 다익스트라
    min_time = dijkstra(N, K)
    return min_time


def dijkstra(start, end):
    # 최대시간
    inf = float('inf')
    # 걸리는 시간 리스트
    time_list = [inf for _ in range(100001)]
    time_list[start] = 0
    # 큐
    queue = [[0, start]]
    while True:
        # 큐가 비면 끝
        if not queue:
            return time_list[end]
        # 현재 시간, 위치
        time, idx = heapq.heappop(queue)
        # 현재 시간이 시간 리스트의 시간보다 크면 패스
        if time > time_list[idx]:
            continue
        # 걷기
        # 인덱스 범위 내에 있을 때
        if idx > 0:
            # 뒤로
            if time+1 < time_list[idx-1]:
                # 시간 리스트 최신화
                time_list[idx-1] = time+1
                # 큐에 추가
                heapq.heappush(queue, [time+1, idx-1])
        if idx < 100000:
            # 앞으로
            if time+1 < time_list[idx+1]:
                # 시간 리스트 최신화
                time_list[idx+1] = time+1
                # 큐에 추가
                heapq.heappush(queue, [time+1, idx+1])
        # 순간이동
        # 인덱스 범위 내에 있을 때
        if idx <= 50000 and idx > 0:
            if time < time_list[idx*2]:
                # 시간 리스트 최신화
                time_list[idx*2] = time
                # 큐에 추가
                heapq.heappush(queue, [time, idx*2])


N, K = map(int, input().split())
print(solution(N, K))