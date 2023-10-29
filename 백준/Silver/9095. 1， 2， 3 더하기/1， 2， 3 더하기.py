def solution(n_list):
    # 하나씩 받으면 다시 계산해야 하니까 리스로 받아서 계산하자
    # 리스트 최댓값
    target = max(n_list)
    # 메모
    memo = [0 for _ in range(target+1)]
    # 인덱스 0 은 자신을 더해주는 개념이므로 1 배정
    memo[0] = 1
    # 인덱스 1 은 하나뿐이므로 미리 작성
    memo[1] = 1
    # 인덱스 2 는 1 1 / 2 로 2개
    memo[2] = 2
    i = 3
    while True:
        # 중단 조건
        if i > target:
            return [memo[n] for n in n_list]
        # n이 n + (n-1) 으로 표현되면 n-1 의 가짓수와 같고
        # 2 + (n-2) 으로 표현되면 n-2 의 가짓수와 같음
        # 3도 마찬가지
        # f(n) = f(n-1) + f(n-2) + f(n-3) 이라고 볼 수 있음
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        i += 1


T = int(input())
n_list = [int(input()) for _ in range(T)]
for result in solution(n_list):
    print(result)
