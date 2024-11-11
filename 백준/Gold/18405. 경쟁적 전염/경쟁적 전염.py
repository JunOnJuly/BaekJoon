import sys

input = sys.stdin.readline


def solution(N, K, informs, S, X, Y):
    # 바이러스 위치 탐색
    v_idxs = [[] for _ in range(K+1)]
    for i in range(N):
        for j in range(N):
            if informs[i][j]:
                v_idxs[informs[i][j]].append([i, j])
    
    # X, Y 와 바이러스들 거리 계산
    # 최소 거리 / 최소 바이러스 번호
    min_dist = float('inf')
    min_v = 0
    # 낮은 번호부터 순회
    # 낮은 번호부터 해야 낮은 번호로 먼저 갱신
    for i in range(1, K+1):
        for x, y in v_idxs[i]:
            # 거리
            dist = abs(X-1-x) + abs(Y-1-y)
            # 최소거리 갱신
            if dist < min_dist:
                min_dist = dist
                # 최소 거리가 S 보다 작으면 최소 바이러스 번호 갱신
                if S >= min_dist:
                    min_v = i

    print(min_v)
    

# 입력
N, K = map(int, input().strip().split())
informs = [list(map(int, input().strip().split())) for _ in range(N)]
S, X, Y = map(int, input().strip().split())

solution(N, K, informs, S, X, Y)