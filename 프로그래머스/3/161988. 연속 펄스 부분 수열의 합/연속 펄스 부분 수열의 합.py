from collections import deque


# 연속 펄스 함수 만드는 함수
def make_cont_pulse(sequence):
    for i in range(len(sequence)):
        if i%2:
            sequence[i] *= -1
            
    return sequence


def solution(sequence):
    # 연속 펄스 함수
    cont_pulse = deque(make_cont_pulse(sequence))

    ## 이전 까지의 최댓값을 다음 값에 넘겨주는 방식
    # DP 테이블
    table = [[max([0, cont_pulse[0]])], [max([-cont_pulse[0], 0])]]
    
    # 순회하며 테이블 채우기
    for i in range(1, len(sequence)):
        table[0].append(max([0, table[0][i-1] + sequence[i]]))
        table[1].append(max([0, table[1][i-1] - sequence[i]]))
    
    return max(table[0] + table[1])
    
    