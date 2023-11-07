def solution(N, K, data_list):
    # 거꾸로 탐색하기 위해 리버스
    data_list = sorted(data_list, reverse=True)
    # 동전의 수
    coin_num = 0
    # 값이 큰 동전부터 탐색
    for val in data_list:
        # 남은 가치보다 낮은 가치의 동전이 있으면
        if K >= val:
            coin_num += K//val
            K %= val

        # 남은 가치가 0이면 끝
        if not K:
            return coin_num


N, K = map(int, input().split())
data_list = [int(input()) for _ in range(N)]
print(solution(N, K, data_list))