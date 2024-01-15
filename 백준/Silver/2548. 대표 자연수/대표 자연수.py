def solution(N, data_list):
    # 데이터 정렬
    data_list = sorted(data_list)
    # 어떤 수보다 큰 수와 작은수의 개수를 따지는 것이 중요
    # 중간수
    print(data_list[(N-1)//2])
    return


N = int(input())
data_list = list(map(int, input().split()))
solution(N, data_list)