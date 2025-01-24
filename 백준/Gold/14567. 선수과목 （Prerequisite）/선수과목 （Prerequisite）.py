import sys
from collections import deque

input = sys.stdin.readline


def solution(N, M, subjects):
    # 위상정렬 리스트 / [[들어오는 노드], 이수한 학기, [나가는 노드]]
    topol_list = [[set(), 0, set()] for _ in range(N+1)]
    for A, B in subjects:
        topol_list[A][2].add(B)
        topol_list[B][0].add(A)
    
    # 큐
    q = deque()
    # 학기
    cnt = 1
    # 순회
    while True:
        # 노드 순회
        for node in range(1, len(topol_list)):
            # 나가는 노드가 없고
            if not topol_list[node][0]:
                # 이수하지 않았으면
                if not topol_list[node][1]:
                    # 큐에 삽입
                    q.append(node)
                    # 학기 갱신
                    topol_list[node][1] = cnt
        
        # 큐가 비면 끝
        if not q:
            break

        # 순회
        while q:
            # 현재 노드
            now_node = q.popleft()
            # 연결된 노드 순회
            for next_node in topol_list[now_node][2]:
                # 선수 과목 제거
                topol_list[next_node][0].remove(now_node)

        # 학기 더해죽
        cnt += 1

    print(*[topol_list[node][1] for node in range(1, len(topol_list))])


# 입력
N, M = map(int, input().strip().split())
subjects = [list(map(int, input().strip().split())) for _ in range(M)]

solution(N, M, subjects)