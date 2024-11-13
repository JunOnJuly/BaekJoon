import sys
import heapq

input = sys.stdin.readline


def solution(N, bundles):
    # 번들 리스트 힙으로 치환
    heapq.heapify(bundles)
    # 카운트
    cnt = 0
    # 모든 번들을 합할 때 까지
    while len(bundles) > 1:
        # 두 개의 번들
        first_bundle = heapq.heappop(bundles)
        second_bundle = heapq.heappop(bundles)
        # 새로운 번들
        new_bundle = first_bundle + second_bundle
        # 추가
        heapq.heappush(bundles, new_bundle)
        # 카운트 추가
        cnt += new_bundle

    print(cnt)


# 입력
N = int(input().strip())
bundles = [int(input().strip()) for _ in range(N)]

solution(N, bundles)