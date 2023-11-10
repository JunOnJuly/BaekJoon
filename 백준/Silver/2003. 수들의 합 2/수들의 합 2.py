def solution(N, M, data_list):
    # 누적합을 편하게 만들기 위해 0 추가
    data_list = [0] + data_list
    # 누적합 생성
    for idx in range(1, len(data_list)):
        # 누적합
        data_list[idx] += data_list[idx-1]
    # 투포인터
    start = 0
    end = 1
    # 카운트
    cnt = 0
    while True:
        # end 가 인덱스를 벗어나면
        if end >= len(data_list):
            return cnt
        # 포인터 값
        start_value = data_list[start]
        end_value = data_list[end]
        # 누적합
        subsum = end_value - start_value
        # 누적합이 목표값보다 크면
        if subsum > M:
            start += 1
            continue
        # 누적합이 목표값보다 작으면
        elif subsum < M:
            end += 1
            continue
        # 누적합이 목표값이면
        else:
            cnt += 1
            end += 1
            continue


N, M = map(int, input().split())
data_list = list(map(int, input().split()))
print(solution(N, M, data_list))