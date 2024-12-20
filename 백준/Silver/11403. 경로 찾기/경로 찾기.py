import sys

input = sys.stdin.readline


def solution(N, mat):
    ## 플로이드-워셜
    # 중간 노드
    for c in range(N):
        # 시작 노드
        for f in range(N):
            # 끝 노드
            for b in range(N):
                # 시작 - 중간 / 중간 - 끝 이 이어져 있으면
                if mat[f][c] and mat[c][b]:
                    # 시작 - 끝도 이어져 있음
                    mat[f][b] = 1

    for i in mat:
        print(*i)


# 입력
N = int(input().strip())
mat = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, mat)