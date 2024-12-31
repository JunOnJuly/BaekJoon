import sys
import heapq as hq

input = sys.stdin.readline


# 거리를 계산하는 함수
def cal_dist(x1, y1, x2, y2):
    dx = x1-x2
    dy = y1-y2

    return pow(pow(dx, 2) + pow(dy, 2), 1/2)


def solution(x1, y1, x2, y2, N, vils):
    # 마을 상에서 최대 거리 : [-3000, -3000] ~ [3000, 3000]
    max_dist = int(cal_dist(-3000, -3000, 3000, 3000))
    ## 최대 거리 이하의 소수 모두 찾기
    # 소수 판정 리스트
    is_prime = [1 for _ in range(max_dist+1)]
    is_prime[0] = 0
    is_prime[1] = 0
    # 에라토스테네스의 체
    for num in range(int(pow(len(is_prime), 1/2))+1):
        # 현재 수가 소수면
        if is_prime[num]:
            # 배수 모두 비소수 체크
            for n in range(2*num, len(is_prime), num):
                is_prime[n] = 0
    
    # 마을에 위치 넣기
    vils = [[x1, y1]] + vils + [[x2, y2]]
    # 그래프
    graph = [[] for _ in range(len(vils))]
    for i in range(len(vils)-1):
        for j in range(i+1, len(vils)):
            # 거리
            dist = int(cal_dist(*vils[i], *vils[j]))
            # 거리가 소수면
            if is_prime[dist]:
                # 그래프에 저장
                graph[i].append([j, dist])
                graph[j].append([i, dist])
    
    ## 다익스트라
    # 큐
    q = [[0, 0]]
    # 최단거리 목록
    min_dists = [float('inf') for _ in range(len(vils))]
    # 순회
    while q:
        # 현재 거리 / 현재 노드
        now_dist, now_node = hq.heappop(q)
        # 현재 거리가 현재 노드의 최단거리보다 길면 패스
        if now_dist > min_dists[now_node]:
            continue

        # 이동 가능 위치 순회
        for next_node, dist in graph[now_node]:
            # 다음 거리
            next_dist = now_dist + dist
            # 다음 거리가 다음 노드까지의 최단거리보다 짧으면
            if next_dist < min_dists[next_node]:
                # 최단거리 갱신
                min_dists[next_node] = next_dist
                # 큐에 추가
                hq.heappush(q, [next_dist, next_node])
    
    print(min_dists[-1] if min_dists[-1] != float('inf') else -1)
    

# 입력
x1, y1, x2, y2 = map(int, input().strip().split())
N = int(input().strip())
vils = [list(map(int, input().strip().split())) for _ in range(N)]

solution(x1, y1, x2, y2, N, vils)