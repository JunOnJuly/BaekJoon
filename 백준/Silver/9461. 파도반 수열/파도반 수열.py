def solution(T, data_list):
    # 데이터 리스트 중 최댓값
    max_list = max(data_list)
    # DP
    memo = [0 for _ in range(101)]
    # 앞부분 채우기
    memo[0:6] = [1, 1, 1, 1, 2, 2]

    i = 6
    while True:
        # 중단조건
        if i == max_list + 1:
            break
        # 점화식
        memo[i] = memo[i-5] + memo[i-1]
        i += 1

    # 출력
    for data in data_list:
        print(memo[data])


T = int(input())
data_list = [int(input()) for _ in range(T)]
solution(T, data_list)

'''
그림을 통해 6~10 번째 삼각형을 분석해보자면
6 번째 삼각형은 1,5 번째 삼각형의 변을 더하고
7 번째 삼각형은 2,6 번째 삼각형의 변을 더하고
.
.
.
n 번째 삼각형은 n-5,n-1 번째 삼각형의 변을 더한다
그렇다면 n <= 5 인 경우는 음수 인덱스를 어떻게 처리할 것인가 에 대해
규칙대로 더해야 할 인덱스를 정리한 후 음수 인덱스의 값을 임의로 정해 처리한다
혹은 5번째 인덱스까지 미리 채워두면 쉽게 해결할 수 있다

index      -3    -2     -1      0       1       2       3      4      5     6     7    8      9    10    11
value       0     0      1      1       1       1       1      2      2     3     4    5      7    9     12
index_sum                             -4,0 / -3,1 /  -2,2 / -1,3 /  0,4 / 1,5 / 2,6 / 3,7 / 4,8 / 5,9 / 6,10
'''