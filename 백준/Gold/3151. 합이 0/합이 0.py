import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def solution(N, points):
    # 점수 정렬
    points = sorted(points)
    # 개수
    cnt = 0
    # l 포인터
    for l in range(N-2):
        # r 포인터
        for r in range(l+2, N):
            # 양 끝 포인터 합
            sum_points = points[l] + points[r]
            # - 포인터 합 찾기
            left_find = bisect_left(points, -sum_points, l+1, r) 
            right_find = bisect_right(points, -sum_points, l+1, r)

            # 두 포인터의 값이 같으면
            if left_find == right_find:
                # 해당하는 값이 없을 경우
                if left_find >= r or points[left_find] != -sum_points:
                    # 패스
                    continue
                    
                # 해당하는 값이 하나일 경우
                else:
                    cnt += 1
            
            # 두 포인터의 값이 다르면
            else:
                # 해당하는 값이 여러 개
                cnt += right_find - left_find
    
    print(cnt)


# 입력
N = int(input().strip())
points = list(map(int, input().strip().split()))

solution(N, points)