def solution(N, data_list):
    # 시작시간에 맞추면 최대 회의수를 구할 수 없음
    # 1~4, 2~3, 3~4 가 있으면 1~4 는 1번 2~3, 3~4 는 2번
    # 끝나는 시간에 맞춰 정렬해야 한다
    # 끝나는 시간이 1순위, 시작시간이 2순위로 정렬
    data_list = sorted(data_list, key=lambda x:(x[1], x[0]))
    # 끝나는 시간
    end = 0
    # 데이터 인덱스
    idx = 0
    # 회의 수
    count = 0
    while True:
        # 총 회의 탐색 리스트를 벗어나면
        if idx >= len(data_list):
            return count
        # 회의 시작시간이 전 끝나는시간보다 길면
        if data_list[idx][0] >= end:
            # 끝난 시간 최신화
            end = data_list[idx][1]
            # 회의 횟수 + 1
            count += 1 
            # 인덱스 하나 뒤로
            idx += 1
        # 아니면
        else:
            idx += 1


N = int(input())
data_list = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, data_list))