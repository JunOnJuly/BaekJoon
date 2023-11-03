def solution(n, data_list):
    # 인덱스 맞춰주기
    data_list = [0] + data_list.copy()
    # DP
    # 첫 줄은 현재까지 최장 부분 수열의 길이를 기록
    # 두 번째 줄은 현재까지 부분수열에서의 최대 합을 기록 
    memo = [[0 for _ in range(n+1)] for _ in range(2)]
    # 앞 부분 기록
    memo[0][1] = 1
    memo[1][1] = data_list[1]
    # 인덱스를 이동하면서 메모 최신화
    for idx in range(2, n+1):
        # 현재 인덱스에서 내려가면서 탐색
        # 수열 합 최댓값
        max_subsum = 0
        for idx_reverse in range(idx-1, 0, -1):
            # 현재 인덱스의 데이터값이 거꾸로 탐색하던 인덱스의 데이터값보다 크다면
            # 현재 인덱스의 수열 길이 최신화
            # 현재 인덱스의 수열 합 최댓값 최신화
            if data_list[idx_reverse] < data_list[idx]:
                if not memo[0][idx]:
                    memo[0][idx] = memo[0][idx_reverse] + 1
                # 최댓값 최신화
                if max_subsum < memo[1][idx_reverse] + data_list[idx]:
                    max_subsum = memo[1][idx_reverse] + data_list[idx]

            # 현재 인덱스의 데이터값보다 작은 값이 없다면
            # 수열 길이 1
            # 수열 합 데이터값
            if idx_reverse == 1:
                if max_subsum:
                    memo[1][idx] = max_subsum
                else:
                    memo[0][idx] = 1
                    memo[1][idx] = data_list[idx]


    return max(memo[1])


n = int(input())
data_list = list(map(int, input().split()))
print(solution(n, data_list))