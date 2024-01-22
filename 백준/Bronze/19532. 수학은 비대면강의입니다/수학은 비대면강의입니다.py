def solution(data_list):
    # 데이터 정리
    a, b, c, d, e, f = data_list
    # 순회
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            # 두개의 식을 모두 만족하면
            if a*x + b*y == c and d*x + e*y == f:
                print(f'{x} {y}')


data_list = list(map(int, input().split()))
solution(data_list)