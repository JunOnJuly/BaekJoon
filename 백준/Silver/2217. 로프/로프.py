def solution(N, data_list):
    # 리스트 정렬
    data_list = sorted(data_list)
    # 최댓값
    max_value = 0
    # 정렬 후 낮은 밧줄부터 제거하면서 비교
    # 중간값만 빼볼 필요는 없음
    for idx in range(N):
        # 제일 낮은 값 X 밧줄 수
        value_sum = data_list[idx] * (N-idx)
        if value_sum > max_value:
            max_value = value_sum
    
    return max_value


N = int(input())
data_list = [int(input()) for _ in range(N)]
print(solution(N, data_list))