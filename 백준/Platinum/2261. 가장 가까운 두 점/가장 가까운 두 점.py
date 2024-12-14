import sys

input = sys.stdin.readline
      

# 거리 계산
def cal_dist(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]

    return dx**2 + dy**2


# 분할 정복
def divide(points, left, right):
    # 범위내 거리를 구할 수 없으면
    if left >= right:
        return float('inf')
    
    # 범위내 거리가 하나면
    elif right - left == 1:
        return cal_dist(points[right], points[left])
    
    # 중앙
    half = (left + right) // 2
    # 최소 거리
    min_dist = min(divide(points, left, half), divide(points, half, right))
    # 중심부터 최소거리만큼 떨어진 범위 내부의 점들 구하기
    candid_list = [points[i] for i in range(left, right+1) 
                   if (points[half][0] - points[i][0])**2 < min_dist]
    # y 정렬
    candid_list.sort(key=lambda x:x[1])
    # 순회
    for l in range(len(candid_list)-1):
        for r in range(l+1, len(candid_list)):
            # y 거리가 최소 거리보다 길면 패스
            if (candid_list[l][1] - candid_list[r][1])**2 < min_dist:
                # 최단거리 갱신
                min_dist = min(min_dist, cal_dist(candid_list[l], candid_list[r]))

            else:
                break

    return min_dist 


def solution(n, points):
    # x 기준으로 정렬
    points.sort(key=lambda x:x[0])
    # 분할 정복
    print(divide(points, 0, n-1))


# 입력
n = int(input().strip())
points = [list(map(int, input().strip().split())) for _ in range(n)]

solution(n, points)