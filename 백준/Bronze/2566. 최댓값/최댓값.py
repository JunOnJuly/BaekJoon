def solution(data_list):
    # 최댓값
    max_num = -1
    # 최대 인덱스
    max_idx = []
    # 순회
    for i in range(9):
        for j in range(9):
            # 현재 값이 최댓값보다 크면 최신화
            if data_list[i][j] > max_num:
                # 최댓값
                max_num = data_list[i][j]
                # 최대 인덱스
                max_idx = [i+1, j+1]
    print(max_num)
    print(*max_idx)
    
    
data_list = [list(map(int, input().split())) for _ in range(9)]
solution(data_list)