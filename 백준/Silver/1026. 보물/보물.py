def solution(N, A, B):
    # 리스트 정렬
    A = sorted(A)
    B = sorted(B, reverse=True)
    # 작은건 큰거랑, 큰건 작은거랑 곱해서 더하는게 제일 작음
    min_sum = 0
    # 곱해서 더해줌
    for a, b in zip(A, B):
        min_sum += a*b

    return min_sum


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solution(N, A, B))