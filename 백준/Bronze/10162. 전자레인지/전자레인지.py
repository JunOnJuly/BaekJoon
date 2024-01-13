from collections import deque


def solution(T):
    # DFS 로 풀기
    # 큐 / queue[i] = [시간, [버튼 누른 횟수 리스트]]
    queue = deque([[0, [0, 0, 0]]])
    # T 가 10의 배수가 아니면 끝
    if T%10:
        print(-1)
        return
    # 순회
    while True:
        # 현재 시간, 횟수 리스트
        now_time, cnt_list = queue.popleft()
        # 각 버튼 누르는 경우 탐색
        for idx, time in enumerate([300, 60, 10]):
            # 시간이 초과되지 않으면 큐에 추가
            if now_time+time < T:
                queue.append([now_time+time, [cnt_list[i] if i != idx else cnt_list[i]+1 for i in range(len(cnt_list))]])
            # 시간이 일치하면 끝
            elif now_time+time == T:
                print(*[cnt_list[i] if i != idx else cnt_list[i]+1 for i in range(len(cnt_list))])
                return
            
            
T = int(input())
solution(T)