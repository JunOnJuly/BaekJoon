def solution(N):
    # DP
    memo = [0 for _ in range(1000001)]
    # 앞 부분만 미리 작성
    memo[2] = 1
    memo[3] = 1
    # 3 보다 작으면
    if N <= 3:
        return memo[N], find_min_list(N, memo[:4])
    
    i = 4
    while True:
        # 종료 조건
        if i == N+1:
            return memo[N], find_min_list(N, memo)
        # 후보 리스트
        candid_list = []
        # i-1
        candid_list.append(memo[i-1])
        # i//2
        if not i%2:
            candid_list.append(memo[i//2])
        # i//3
        if not i%3:
            candid_list.append(memo[i//3])
        
        # 최솟값
        memo[i] = min(candid_list) + 1

        i+=1


# 최솟값이 되는 리스트 찾기
def find_min_list(N, memo):
    # 최솟값
    min_n = memo[-1]
    # 경로 리스트
    route_list = [N]

    i = N
    while True:
        # 종료 조건
        if i == 1:
            return route_list
        # 조건 탐색
        # i//2
        if not i%2 and memo[i//2] == memo[i]-1:
            route_list.append(i//2)
            i //= 2
        # i//3
        elif not i%3 and memo[i//3] == memo[i]-1:
            route_list.append(i//3)
            i //= 3
        # i-1
        else:
            route_list.append(i-1)
            i -= 1


N = int(input())
n, n_list = solution(N)
print(n)
print(*n_list)