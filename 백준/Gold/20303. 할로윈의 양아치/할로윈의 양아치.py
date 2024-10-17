import sys
from collections import defaultdict

input = sys.stdin.readline
    

# 아이들의 그룹을 구하기 위한 유니온 파인드
# 유니온
def Union(child_1, child_2, group_list):
    # 아이들의 그룹
    group_1 = Find(child_1, group_list)
    group_2 = Find(child_2, group_list)
    # 두 아이의 그룹이 같으면
    if group_1 == group_2:
        # 리턴
        return False, group_list
    
    # 두 아이의 그룹이 다르면
    else:
        # 그룹이 작은 쪽으로 병합
        if group_1 < group_2:
            group_list[group_2] = group_1
        else:
            group_list[group_1] = group_2
        
        # 리턴
        return True, group_list
    

# 파인드
def Find(child, group_list):
    # 자신의 그룹이 자신이 아니면
    if group_list[child] != child:
        # 그룹을 거슬러 올라가며 최신화
        group_list[child] = Find(group_list[child], group_list)
    
    # 리턴
    return group_list[child]


def solution(N, M, K, candies, edges):
    # 그룹 리스트
    group_list = list(range(N))
    # 엣지 순회하며 그룹 분할
    for child_1, child_2 in edges:
        state, group_list = Union(child_1, child_2, group_list)
    
    # 그룹 당 사람 수 / 캔디 개수
    candies_per_group = defaultdict(lambda : [0, 0])
    for i in range(N):
        candies_per_group[Find(i, group_list)][0] += 1
        candies_per_group[Find(i, group_list)][1] += candies[i]
    
    # 리스트로 치환
    candies_per_group = list(candies_per_group.values())
    # 냅색 알고리즘
    memo = [[0 for _ in range(K)] for __ in range(len(candies_per_group)+1)]
    # 순회
    for i in range(1, len(candies_per_group)+1):
        for j in range(1, K):
            # 사람 수 / 캔디 수
            p_num, c_num = candies_per_group[i-1]
            # j 가 사람 수 이상일 때만
            if j >= p_num:
                # 직전까지의 최대 사탕 수와 자신이 포함 되었을 때 최대 사탕수와 비교
                memo[i][j] = max(memo[i-1][j], memo[i-1][j-p_num] + c_num)
            # j 가 사람 수 이하면
            else:
                # 이전의 최댓값
                memo[i][j] = memo[i-1][j]
                
    print(memo[-1][-1])


# 입력
N, M, K = map(int, input().strip().split())
candies = list(map(int, input().strip().split()))
edges = [list(map(lambda x: int(x)-1, input().strip().split())) for _ in range(M)]

solution(N, M, K, candies, edges)