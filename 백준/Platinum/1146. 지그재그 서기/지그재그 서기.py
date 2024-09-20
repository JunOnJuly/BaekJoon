import sys

input = sys.stdin.readline


def solution(N):
    # N 명의 학생이 존재하고 P 자리에 N 번째 학생이 존재하는 경우를
    # A_NP 라고 하자
    # N 이 P 자리에 위치하는 경우를 생각해보면

    # P == 1 즉 N 이 첫번째 자리에 위치하면
    # 남아있는 수는 모두 N 보다 작으므로 큰수(N) - 작은수 - 큰수 - .. 의 형식을 띈다
    # 남아있는 수 중 가장 큰 수인 N-1 은 큰수의 위치에 존재해야 한다
    # -> 작은수의 위치에 존재하면 큰 수의 위치에 다른 수가 존재할 수 없으므로
    # N 이 P == 1 의 자리에 위치하는 경우 경우의 수는
    # 작은수 - 큰수 - ... 의 수열이며
    # N-1 은 짝수번째에 위치하는 경우의 수와 같음

    # P == 2 즉 N 이 두번째 자리에 위치하면
    # 남아있는 수는 모두 N 보다 작으므로 작은수 - 큰수(N) - 작은수 - ... 의 형식을 띈다
    # 남아있는 수 중 가장 큰 수인 N-1 은 1 번 인덱스 혹은 P+1 즉 세번째 자리부터 오는
    # 작은수 - 큰수 - ... 의 수열에서 큰수의 위치에 존재
    # -> 위의 논리와 같은 논리
    # N 이 P == 2 의 자리에 위치하는 경우 경우의 수는
    # 작은수 - 큰수 - ... 의 수열이며
    # 양 옆에 크기가 1, N-2 의 크기를 갖고 큰수 <- 작은수, N, 작은수 -> 큰수 의 수열을 갖게 되므로
    # 양 옆에 있는 수열의 경우의 수를 곱해준 값에 N-1 개의 수 중 1 개를 뽑는 경우를 곱해준 값과 같음

    #...
    
    # P == K (1 <= K <= N) 의 자리에 위치하면
    # 남아있는 수는 N 보다 작으므로 어차피 N 의 양쪽에 존재하는 수열은 형태가 정해져있다
    # 또 양 옆에 있는 수열의 경우의 수를 곱한 경우의 수에 한쪽에 들어갈 수를 정하는 경우의 수를 곱한 만큼 경우의 수가 존재함
    # A_NP = sum([A_(P-1)(p) for p in range(1, P)])/2 * sum([A_(N-P)(p) for p in range(1, N-P-1)])/2 * (N-1)_C_(P-1)
    #      = A_(P-1)p/2 * A_(N-P)p/2 * (N-1)_C_(P-1)
    # /2 를 해주는 이유는 수열의 형태가 정해져있기 때문
    # -> 큰수 - 작은수 - ... 의 경우의 수는 작은수 - 큰수 - ... 의 수와 같기 때문
    # 수열의 수가 0, 1 과 같이 두가지 경우로 나눠지지 않으면 나눌 필요 없음
    # -> 사실 남아있는 수 중에 가장 큰 수가 무엇인지는 중요하지 않음
    # -> 어차피 크고 작음만 중요하기 때문

    # 총 경우의 수 = sum([A_NP for P in range(1, N+1)])

    # DP / memo[N][P] = A_NP = N 명중 P 번째에 N 번째 학생이 있을 경우
    memo = [[0 for _ in range(N+1)] for __ in range(N+1)]
    memo[0][0] = 1
    memo[1][1] = 1
    # 순회하면서 채우기
    for n in range(2, N+1):
        for p in range(1, n+1):
            # (n-1)_C_(p-1)
            comb = 1
            for num in range(p-1):
                comb *= n-1-num
            for num in range(1, p):
                comb //= num
            # p == 1 / 2 / n-1 / n 일때
            if p <= 2 or p >= n-1:
                # 둘 다 일때
                if p <= 2 and p >= n-1:
                    # 둘 다 나눠주지 않음
                    # 어차피 수열의 형태가 한가지씩 뿐
                    memo[n][p] = (sum(memo[p-1]) * sum(memo[n-p])) * comb
                # 둘 중 하나일때
                else:
                    # 둘 중 하나만 나눠줌
                    # 둘 중 하나만 수열의 형태가 큰-작 / 작-큰 으로 두배
                    memo[n][p] = (sum(memo[p-1]) * sum(memo[n-p])) // 2 * comb
            # 둘 다 아닐때
            else:
                # 둘 다 나눠줌
                memo[n][p] = (sum(memo[p-1]) * sum(memo[n-p])) // 4 * comb

    return sum(memo[-1]) % 1000000


# 입력
N = int(input().strip())
print(solution(N))