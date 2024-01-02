def solution(N, M, A, B):
    subset_A = set(A)-set(B)
    subset_B = set(B)-set(A)
    print(len(subset_A) + len(subset_B))


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
solution(N, M, A, B)