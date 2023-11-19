def solution(N, data_list):
    # 데이터 리스트 정렬
    # 누적합 리스트 만들기 위해 0 추가
    data_list = [0] + sorted(data_list)
    # 누적합으로 변경
    for idx in range(len(data_list)):
        # 0 번 인덱스 스킵
        if idx:
            data_list[idx] += data_list[idx-1]
    # 누적합 모두 더하기
    return sum(data_list)


N = int(input())
data_list = list(map(int, input().split()))
print(solution(N, data_list))