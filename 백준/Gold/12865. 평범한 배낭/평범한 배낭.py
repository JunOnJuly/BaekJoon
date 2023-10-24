# 배낭문제 (냅색 알고리즘)
def solution(N, K, objects):
    # 정렬
    objects = sorted(objects, key=lambda x: (x[0], x[1]))
    # 2차원 DP
    memo = [[0 for _ in range(N+1)] for __ in range(K+1)]
    
    # 메모의 크기에 맞게
    for i in range(N+1):
        for j in range(K+1):
            # [i-1] -> 인덱스 맞추려고
            if i and j >= objects[i-1][0]:
                # 현재 물체를 가방에 넣지 않았을 때 가치와
                # 물체를 넣지 않았을 때 가방 안의 최대 가치 + 물체의 가치
                # 둘 중 높은 가치로 결정
                memo[j][i] = max(memo[j][i-1], max(memo[j-objects[i-1][0]][:i]) + objects[i-1][1])
            # 현재 물체보다 가벼운경우는 이전 물체까지의 최대무게를 채워줌
            elif i and j < objects[i-1][0]:
                memo[j][i] = memo[j][i-1]
    # 메모 마지막 리턴
    return memo[-1][-1]

    
N, K = map(int, input().split())
objects = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, K, objects))