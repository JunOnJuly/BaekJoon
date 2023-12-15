import heapq
import math


def solution(n, data_list):
    # 거리 맵
    dist_map = [[0 for __ in range(n)] for _ in range(n)]
    # 거리 맵 구성
    for i in range(len(data_list)-1):
        for j in range(i+1, len(data_list)):
            # x, y 좌표 차
            sub_ij_x = data_list[i][0] - data_list[j][0]
            sub_ij_y = data_list[i][1] - data_list[j][1]
            # 거리
            dist = round(math.sqrt(sub_ij_x**2 + sub_ij_y**2), 2)
            # 거리 입력
            dist_map[i][j] = dist
    # kruskal
    print(kruskal(n, dist_map))


# kruskal
def kruskal(n, dist_map):
    # 루트 리스트
    union_list = list(range(n))
    # 큐
    queue = []
    # 큐에 거리 삽입
    for i in range(len(dist_map)):
        for j in range(len(dist_map)):
            if dist_map[i][j]:
                heapq.heappush(queue, [dist_map[i][j], i, j])
    # 거리 합
    dist_sum = 0
    # 작은 거리부터 삽입
    while True:
        # 큐가 비면 끝
        if not queue:
            return dist_sum
        # 거리, 인덱스1, 인덱스2
        dist, i, j = heapq.heappop(queue)
        # 순환이 아니면 삽입
        state, union_list = union(union_list, i, j)
        if state:
            dist_sum += dist


# find
def find(union_list, num):
    # 자신의 부모가 자신이면 리턴
    if union_list[num] == num:
        return num
    # 아니면 루트를 최신화 및 재귀
    else:
        union_list[num] = find(union_list, union_list[num])
    return union_list[num]


# union
def union(union_list, num1, num2):
    # 각 노드의 루트
    root_1 = find(union_list, num1)
    root_2 = find(union_list, num2)
    # 루트가 같으면 순환이므로 리턴
    if root_1 == root_2:
        return False, union_list
    # 다르면 합침
    else:
        union_list[root_2] = root_1
        return True, union_list


n = int(input())
data_list = [list(map(float, input().split())) for _ in range(n)]
solution(n, data_list)