import sys
input = sys.stdin.readline


def solution(N, hs):
    # 카운트 / 맨 앞은 무조건 보임
    cnt = 1
    # 현재까지 가장 큰 길이
    max_height = hs.pop()
    # 순회
    while hs:
        # 마지막 길이
        last_height = hs.pop()
        # 현재 가장 큰 길이보다 마지막 길이가 작으면 패스
        if last_height <= max_height:
            continue
        # 가장 큰 길이보다 길면
        else:
            # 카운트 + 1
            cnt += 1
            # 가장 큰 길이 최신화
            max_height = last_height
    print(cnt)

    
N = int(input())
hs = [int(input()) for _ in range(N)]
solution(N, hs)