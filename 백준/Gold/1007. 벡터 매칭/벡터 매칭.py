from itertools import combinations

def solution(N, vector_list):
    # 주어진 벡터중 절반은 더하고 절반은 빼는 형식임
    # 결국 모든 벡터중에 뺄 절반과 더할 절반의 경우의 수를 구하면 됨
    # 인덱스를 뽑기 위한 인덱스 리스트
    idx_list = list(range(len(vector_list)))

    # 벡터 길이 리스트
    vector_sum_list = []
    # 모든 경우
    for pos_idx in combinations(idx_list, len(idx_list)//2):
        # 벡터 합
        sum_x = 0
        sum_y = 0
        # 더해질 벡터 인덱스
        pos_idx_set = set(pos_idx)
        # 빼질 벡터 리스트
        neg_idx_set = set(idx_list) - pos_idx_set
        neg_idx = list(neg_idx_set)
        # 벡터에 더해주고
        for idx in pos_idx:
            sum_x += vector_list[idx][0]
            sum_y += vector_list[idx][1]
        # 벡터에서 빼주고
        for idx in neg_idx:
            sum_x -= vector_list[idx][0]
            sum_y -= vector_list[idx][1]
        # 길이 구해서 리스트에 추가
        vector_sum_list.append(((sum_x**2)+(sum_y**2))**(1/2))
    return min(vector_sum_list)


T = int(input())
for _ in range(T):
    N = int(input())
    vector_list = [list(map(int, input().split())) for __ in range(N)]
    print(solution(N, vector_list))