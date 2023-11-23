from itertools import combinations


def solution(N, M, data_list):
    # 치킨집 리스트, 집 리스트 정리
    all_chick_list = []
    house_list = []
    for i in range(N):
        for j in range(N):
            if data_list[i][j] == 1:
                house_list.append([i, j])
            elif data_list[i][j] == 2:
                all_chick_list.append([i, j])
    # 도시의 치킨 거리
    city_chick_dist = 1300
    # 가능한 조합을 돌아가면서 도시의 치킨 거리 구함
    for chick_list in combinations(all_chick_list, M):
        # 현재 조합의 도시의 치킨 거리
        temp_city_chick_dist = 0
        for house in house_list:
            # 치킨 거리들을 더함
            temp_city_chick_dist += find_chick_dist(house, chick_list)
        # 도시의 치킨 거리 최신화
        if city_chick_dist > temp_city_chick_dist:
            city_chick_dist = temp_city_chick_dist
    return city_chick_dist


# 치킨 거리를 구하는 함수
def find_chick_dist(house, chick_list):
    # 치킨 거리
    chick_dist = 100
    # 순회하면서 업데이트
    for chick in chick_list:
        # 거리 계산
        dist = cal_dist(house, chick)
        if dist < chick_dist:
            chick_dist = dist
    return chick_dist


# 거리를 구하는 함수
def cal_dist(idx1, idx2):
    # 좌표 정리
    x1, y1 = idx1
    x2, y2 = idx2
    return abs(x1-x2) + abs(y1-y2)


N, M = map(int, input().split())
data_list = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, data_list))