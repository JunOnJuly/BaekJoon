def solution(n, data_list):
    # 인덱스 맞춰주기
    data_list = [0] + data_list
    # DP
    memo = [0 for _ in range(100001)]
    # 현재 인덱스를 포함한 최댓값
    sub_memo = [0 for _ in range(100001)]
    # memo 1 채우기
    memo[1] = data_list[1]
    sub_memo[1] = data_list[1]
    # 탐색
    for idx in range(2, n+1):
        # 하나 전까지의 현재 인덱스를 포함하는 메모와 현재 인덱스의 값의 합
        # 해당 인덱스의 값
        # 둘 중 최대를 현재 인덱스를 포함하는 메모에 삽입
        sub_memo[idx] = max(sub_memo[idx-1]+data_list[idx], data_list[idx])
        # 현재 인덱스를 포함하는 메모의 값
        # 전까지의 최댓값
        # 둘 중 큰 값을 메모에 삽입
        memo[idx] = max(sub_memo[idx], memo[idx-1])


    return memo[n]


n = int(input())
data_list = list(map(int, input().split()))
print(solution(n, data_list))