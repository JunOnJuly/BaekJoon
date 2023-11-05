def solution(N, data_list):
    # DP
    memo = [0 for _ in range(N+1)]
    # 일의 번호, data_list 인덱스
    for work in range(N):
        # n 번째 시작한 일이 끝나는 날
        end_day = work + data_list[work][0]
        # 퇴사하기 전에 끝날 경우에만
        if end_day < N+1:
            # 끝나는 날 부터 퇴사하는 날까지 최댓값 갱신
            for day in range(end_day, N+1):
                memo[day] = max(memo[day], memo[work] + data_list[work][1])


    return memo[-1]


N = int(input())
data_list = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, data_list))