def solution(N):
    # 앞에서부터 메모
    memo = [-1 for _ in range(N+1)]
    # 앞에 1 은 자체니까 0
    memo[1] = 0

    i = 2
    while True:
        # 정지 조건
        if i > N:
            return memo[-1]
        # 가능 목록
        # 3으로 나눠지면 3으로 나눈 인덱스
        # 2로 나눠지면 2로 나눈 인덱스
        # 1보다 크면 1을 뺀 인덱스
        candid_list = []
        if not i%3:
            candid_list.append(memo[i//3])
        if not i%2:
            candid_list.append(memo[i//2])
        if i > 1:
            candid_list.append(memo[i-1])
        # 가능 목록 중 가장 작은거 +1 이 해당 인덱스에 들어갈 수
        memo[i] = min(candid_list)+1
        # 인덱스 + 1
        i += 1


N = int(input())
print(solution(N))