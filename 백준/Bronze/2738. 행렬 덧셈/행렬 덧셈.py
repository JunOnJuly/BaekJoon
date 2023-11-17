def solution(N, M, A, B):
    return_list = []
    for line in range(N):
        temp_line = []
        for a, b in zip(A[line], B[line]):
            temp_line.append(a+b)
        return_list.append(temp_line)
    
    for n in range(N):
        print(*return_list[n])

        
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
solution(N, M, A, B)