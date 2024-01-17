def solution(data_list):
    # 빈 리스트 생성
    char_list = [['' for _ in range(15)] for __ in range(5)]
    # 빈 리스트 채우기
    for i in range(5):
        for j in range(len(data_list[i])):
            char_list[i][j] = data_list[i][j]
    # 출력
    for i in range(15):
        for j in range(5):
            if char_list[j][i] != '':
                print(char_list[j][i], end='')


data_list = [list(input()) for _ in range(5)]
solution(data_list)