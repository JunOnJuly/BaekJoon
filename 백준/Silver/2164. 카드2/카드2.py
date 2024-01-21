from collections import deque


def solution(N):
    # 큐
    queue = deque(list(range(1, N+1)))
    # 순회
    while True:
        # 남은 카드가 한장이면 프린트
        if len(queue) == 1:
            return queue.pop()
        # 맨 위에 있는 카드 버림
        queue.popleft()
        # 맨 위에 있는 카드 맨 아래로
        queue.append(queue.popleft())
       

N = int(input())
print(solution(N))