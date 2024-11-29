import sys
from bisect import bisect_left

input = sys.stdin.readline


# 설정한 값이 가능한지 판단
def is_max_dist(N, C, idxs, max_min_dist):
    # 설치 정보 / [설치 카운트, 설치 위치, 설치 인덱스]
    ins = [1, idxs[0], 0]
    # 앞에서 부터 설치
    while True:
        # 직전 설치 정보
        before_ins_cnt, before_ins, before_ins_idx = ins
        
        # 모두 설치되었으면
        if before_ins_cnt == C:
            return True
        
        # 다음 설치 위치
        next_ins = before_ins + max_min_dist
        # 설치 가능 인덱스
        next_ins_idx = bisect_left(idxs, next_ins)
        # 설치 인덱스가 범위를 벗어나면
        if next_ins_idx >= len(idxs):
            # 중단
            return False
        # 설치 정보 업데이트
        ins = [before_ins_cnt + 1, idxs[next_ins_idx], next_ins_idx]


def solution(N, C, idxs):
    # 인덱스 정렬
    idxs = sorted(idxs)
    # 집 사이의 거리의 최댓값
    max_min_dist = 0
    ## 집 사이의 거리의 최댓값 후보
    # 양 옆 위치
    left = 0
    right = (idxs[-1] - idxs[0]) // (C-1)
    # 간격
    candid_max_min_dist = (right - left)
    # 최댓값을 조정하며 최댓값이 성립하는지 체크
    while left <= right:
        # 최댓값 성립 여부
        is_max = is_max_dist(N, C, idxs, candid_max_min_dist)
        # 해당 최댓값이 성립하면
        if is_max:
            # 최댓값 갱신
            max_min_dist = candid_max_min_dist
            # 왼쪽 위치 상승
            left = candid_max_min_dist + 1
        
        # 해당 최댓값이 성립하지 않으면
        else:
            # 오른쪽 위치 하강
            right = candid_max_min_dist - 1

        # 최댓값 후보 갱신
        candid_max_min_dist = (left + right) // 2

    print(max_min_dist)

    
# 입력
N, C = map(int, input().strip().split())
idxs = [int(input().strip()) for _ in range(N)]

solution(N, C, idxs)