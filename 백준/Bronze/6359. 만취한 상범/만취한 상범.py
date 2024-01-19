def solution(n):
    # 각 약수의 개수만큼 열고닫고 반복
    # 홀수번 반복되면 도망칠 수 있음
    # 약수의 개수가 홀수?
    # 제곱수
    square_primes = list(map(lambda x:x**2, range(1, 11)))
    # n 이하의 수 찾기
    print([square_prime<=n for square_prime in square_primes].count(True))


T = int(input())
for _ in range(T):
    n = int(input())
    solution(n)