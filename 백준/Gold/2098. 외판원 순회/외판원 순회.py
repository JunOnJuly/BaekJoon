import sys
from itertools import combinations

input = sys.stdin.readline


def solution(N, costs):
    # dp 테이블
    dp = {}
    # 갈 수 없는 길은 inf 로 재조정
    for i in range(len(costs)):
        for j in range(len(costs[i])):
            if not costs[i][j]:
                costs[i][j] = float('inf')

    # 임의의 시작 도시(0) 에서 각 도시로 가는 비용 초기화
    for n in range(1, N):
        # [0, n] 만을 방문했고 마지막 도시가 m 인 경우
        dp[(frozenset([0, n]), n)] = costs[0][n]
    
    # 점차 방문 도시를 확장
    for subset_size in range(3, N+1):
        # 조합
        for subset in combinations(range(N), subset_size):
            # 임의의 시작 도시(0)가 포함되어있지 않으면
            if 0 not in subset:
                # 패스
                continue

            # frozenset으로 치환
            subset_fs = frozenset(subset)
            # 마지막 경유지 고르기
            for cur in subset:
                # 임의의 시작 도시(0) 는 경유 도시가 아님
                if cur == 0:
                    continue

                # 마지막 경유지를 제외한 도시 집합
                prev_subset = subset_fs - {cur}
                # 최소 비용
                min_cost = float('inf')
                # 마지막 경유지를 제외한 나머지 도시 중 마지막 도시 고르기
                for prev in prev_subset:
                    # 마지막 도시가 임의의 시작 도시(0)일 가능성은 없으므로 제외
                    if prev == 0:
                        continue

                    # 해당 도시를 마지막으로 하는 최소 거리
                    cost = dp[(prev_subset, prev)] + costs[prev][cur]
                    # 최단 거리 갱신
                    min_cost = min(min_cost, cost)
            
                # 최단 거리 갱신
                dp[(subset_fs, cur)] = min_cost
            
    # 마지막 도시에서 시작 도시로 돌아가는 비용 더해주기
    # 모든 경로
    full_set = frozenset(range(N))
    # 모든 경로 중 최단 거리
    min_cost = min(dp[(full_set, n)] + costs[n][0] for n in range(1, N))

    print(min_cost)
        

N = int(input().strip())
costs = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, costs)