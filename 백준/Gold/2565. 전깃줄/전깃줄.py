import sys

input = sys.stdin.readline


def solution(N, lines):
    # 라인 정리
    lines = [l[1] for l in sorted(lines, key=lambda x:x[0])]
    # 증가하는 최대 부분 수열 길이
    max_inc = [1 for _ in range(N)]
    # 순회
    for l in range(1, N):
        # 자신보다 이전 전선이고 자신보다 작은 목표 전선을 갖고 있는 최대 길이중 최댓값
        # [0] 은 리스트가 빌 때를 대비
        max_inc[l] = max([0] + [max_inc[m] for m in range(l) if lines[m] < lines[l]]) + 1
    
    print(N - max(max_inc))


# 입력
N = int(input().strip())
lines = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, lines)