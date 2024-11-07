import sys
from collections import deque

input = sys.stdin.readline


def solution(p: str, n: int, arr: list) -> None: 
    # 데크로 치환
    arr = deque(arr)
    # 바뀐 횟수
    R_cnt = 0
    # 함수에 RR 이 있으면 원상태므로 삭제
    p.replace('DD', '')
    # 함수 작동
    for chr in p:
        # R
        if chr == 'R':
           # 바뀐 횟수 + 1
           R_cnt += 1
        
        # D
        elif chr == 'D':
            # 비어있으면 에러
            if not arr:
                print('error')
                return
            
            # 작동
            else:
                # 바뀐 횟수가 짝수면
                if not R_cnt%2:
                    # 앞에서 지우기
                    arr.popleft()
                
                # 홀수면
                else:
                    # 뒤에서 지우기
                    arr.pop()
    
    # 바뀐 횟수가 짝수면 그대로 출력
    if not R_cnt%2:
        print('[' + ','.join(map(str, arr)) + ']')
    
    # 짝수면 뒤집어서 출력
    else:
        print('[' + ','.join(map(str, reversed(arr))) + ']')


# 입력
T = int(input().strip())
for _ in range(T):
    p = input().strip()
    n = int(input().strip())
    if n == 0:
        arr = []
        trash = input().strip()
    else:
        arr = list(map(int, input().strip()[1:-1].split(',')))

    solution(p, n, arr)