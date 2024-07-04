from collections import deque


def solution(queue1, queue2):
    # 데크로 치환
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # 길이들
    queue1_len = len(queue1)
    queue2_len = len(queue2)
    all_len = queue1_len + queue2_len
    
    # 총 합이 홀수면 불가
    if sum(queue1 + queue2)%2:
        return -1
    
    # 카운트
    cnt = 0
    
    # 합 비교
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    
    # 합이 큰 큐에서 작은 큐로 하나씩 옮겨보며 비교
    while True:
        # 모든 수가 이동된 경우 끝
        if cnt > all_len * 3:
            return -1
        
        if sum_queue1 > sum_queue2:
            queue2.append(queue1.popleft())
            sum_queue1 -= queue2[-1]
            sum_queue2 += queue2[-1]
            cnt += 1
            
        elif sum_queue1 < sum_queue2:
            queue1.append(queue2.popleft())
            sum_queue1 += queue1[-1]
            sum_queue2 -= queue1[-1]
            cnt += 1
            
        else:
            return cnt