from collections import deque

def solution(A, B):
    # 큐
    queue = deque([[A, 1]])
    # 계산
    while True:
        # 큐가 비면 끝
        if not queue:
            return -1
        # 현재 수, 카운트
        now_num, cnt = queue.popleft()
        # 목적수에 도달하면 리턴
        if now_num == B:
            return cnt
        # 메모 비교 및 최신화
        # x2
        if now_num*2 <= B:
            # 큐에 추가
            queue.append([now_num*2, cnt + 1])
        # x10 + 1
        if now_num*10 + 1 <= B:
            # 큐에 추가
            queue.append([now_num*10 + 1, cnt + 1])


A, B = map(int, input().split())
print(solution(A, B))