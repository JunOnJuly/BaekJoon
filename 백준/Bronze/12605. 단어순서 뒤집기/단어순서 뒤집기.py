def solution(N, data_list):
    # 데이터 순회
    for T, data in enumerate(data_list):
        # 데이터 길이
        data_length = len(data)
        # 단어 뒤에서 순회
        for idx in range(data_length):
            if not idx:
                print(f"Case #{T+1}: ", end='')
            if idx < data_length-1:
                print(data.pop(), end=' ')
            else:
                print(data.pop())



N = int(input())
data_list = [input().split() for _ in range(N)]
solution(N, data_list)