def solution(N, A, B):
    # 리스트 정렬
    A = sorted(A)
    # A를 정렬한 인덱스 리스트와 와 B 를 병합
    A_index_list = list(range(N))
    A_index_list = zip(A_index_list, B)
    # B 에 따라 A_index_list 를 정렬
    A_index_list = sorted(A_index_list, key=lambda x: -x[1])
    # 분리
    A_index_list = [a[0] for a in A_index_list]
    # A 를 A_index_list 를 참고해서 정렬
    temp_A = [0 for _ in range(N)]
    for idx in range(N):
        temp_A[A_index_list[idx]] = A[idx]
    # 곱해서 더해줌
    min_sum = 0
    for a, b in zip(temp_A, B):
        min_sum += a*b

    return min_sum


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(solution(N, A, B))
