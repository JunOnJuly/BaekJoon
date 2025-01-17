import sys
import heapq as hq

input = sys.stdin.readline


def solution(H, W, hs):
    # 높이 리스트 + 인덱스
    hs_idx = [[-hs[h], h] for h in range(len(hs))]
    # 힙으로 만들기
    hq.heapify(hs_idx)
    # 결과
    result = 0
    # 체크 목록
    visited = [1 for _ in range(W)]
    # 가장 높은 위치 탐색
    first_h, first_i = hq.heappop(hs_idx)
    first_h = -first_h
    # 순회
    while hs_idx:
        # 다음으로 가장 높은 위치
        second_h, second_i = hq.heappop(hs_idx)
        second_h = -second_h
        # 다음으로 가장 높은 위치를 체크하지 않았으면
        if visited[second_i]:
            # 순회
            for i in range(min(second_i, first_i), max(second_i, first_i)+1):
                # 체크한 위치가 아니면
                if visited[i]:
                    # 결과 더해주기
                    result += max(0, second_h - hs[i])
                    # 체크
                    visited[i] = 0

        # 가장 높은 위치 교체
        first_h, first_i = second_h, second_i

    print(result)


# 입력
H, W = map(int, input().strip().split())
hs = list(map(int, input().strip().split()))

solution(H, W, hs)