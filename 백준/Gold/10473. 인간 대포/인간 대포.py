import sys
import heapq
import math

input = sys.stdin.readline


# 정보 저장을 위한 클래스
class Node:
    def __init__(self, idxs, is_cannon=True):
        # 현재 x
        self.x = idxs[0]
        # 현재 y
        self.y = idxs[1]
        # 현재 노드까지 최단시간
        self.min_time = float('inf')
        # 대포인지 여부
        self.is_cannon = is_cannon
    

    def __lt__(self, other):
        if self.min_time < other.min_time:
            return True
        return False


    def __str__(self):
        return f'x : {self.x} / y : {self.y} / min_time : {self.min_time}'


# solution
def solution(start_idx, end_idx, nodes):
    # 힙
    hq = [[0, Node(start_idx, False)]]
    # 순회
    while hq:
        # 팝
        now_pop = heapq.heappop(hq)
        # 현재 노드
        now_node = now_pop[1]
        # 현재 노드까지 시간
        now_time = now_pop[0]
        # 현재 좌표
        now_x = now_node.x
        now_y = now_node.y
        # 현재까지 최단 시간
        min_time = now_node.min_time
        # 현재 시간이 현재까지 최단시간보다 길면 패스
        if now_time > min_time:
            continue
        # 연결된 노드 순회
        for cn_node in nodes:
            # 연결된 노드의 좌표
            next_x = cn_node.x
            next_y = cn_node.y
            # 연결된 노드까지의 최단 시간
            next_min_time = cn_node.min_time
            # 연결된 노드까지의 거리
            dist = cal_dist([now_x, now_y], [next_x, next_y])
            # 대포면 연결된 노드까지 가는 두 경로 중 짧은 시간
            if now_node.is_cannon:
                time = min([dist / 5, 2 + abs(50-dist)/5])
            else:
                time = dist / 5
            # 현재까지의 최단거리 + 연결된 노드까지의 거리, 연결된 노드까지의 최단거리와 비교
            # 더 길면 패스
            if now_time + time >= next_min_time:
                continue
            # 짧으면
            # 최단거리 최신화
            cn_node.min_time = now_time + time
            # 힙에 추가
            heapq.heappush(hq, [now_time + time, cn_node])
    
    # 도착 노드
    for node in nodes:
        if node.x == end_idx[0] and node.y == end_idx[1]:
            return node.min_time


# 좌표끼리의 거리를 구하는 함수
def cal_dist(idx1, idx2):
    x1, y1 = idx1
    x2, y2 = idx2

    sum_pows = pow(x1-x2, 2) + pow(y1-y2, 2)

    return math.sqrt(sum_pows)


# 입력
start_idx = list(map(float, input().strip().split()))
end_idx = list(map(float, input().strip().split()))
n = int(input().strip())
nodes = [Node(list(map(float, input().strip().split()))) for _ in range(n)] + [Node(end_idx)]

# 출력
print(solution(start_idx, end_idx, nodes))