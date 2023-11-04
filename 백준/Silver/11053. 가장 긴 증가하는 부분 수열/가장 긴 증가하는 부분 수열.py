def solution(N, data_list):
    # DP
    memo = [1 for _ in range(N)]
    # 첫 부분 작성
    memo[0] = 1

    # 순서대로 최댓값을 늘리고 거꾸로 탐색하면서 메모 최신화
    for idx_now in range(N):
        for idx_reverse in range(idx_now, -1, -1):
            # 현재 인덱스의 값보다 작은 값이 앞에 존재하면 그 값 + 1 메모, 더 큰 값이 존재하면 업데이트
            if data_list[idx_reverse] < data_list[idx_now] and memo[idx_now] <= memo[idx_reverse]:
                memo[idx_now] = memo[idx_reverse]+1
                

    return max(memo)


N = int(input())
data_list = list(map(int, input().split()))
print(solution(N, data_list))