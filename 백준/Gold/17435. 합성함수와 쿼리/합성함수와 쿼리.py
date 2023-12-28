import sys
from math import log2

def solution(m, function_list, Q, data_list):
    # 희소 배열 행 길이
    column_len = int(log2(500000))+1
    # 희소 배열
    sparse_table = [[0] + function_list for _ in range(column_len)]
    # 희소 배열 채우기, sparse_table[i][j] = f_2^i(j)
    for j in range(1, column_len):
        for i in range(1, len(sparse_table[j])):
            sparse_table[j][i] = sparse_table[j-1][sparse_table[j-1][i]]
    # 데이터 리스트를 순회
    for n, x in data_list:
    # n 을 2의 지수로 분해
        n_bin = list(bin(n)[2:])
        # 2진수 길이
        n_len = len(n_bin)
        # 2진수를 순회하며 함수 적용
        for idx in range(n_len):
            # 2진수의 값이 1이면
            if int(n_bin[idx]):
                # x = 함숫값
                x = sparse_table[n_len-1-idx][x]
        print(x)


m = int(sys.stdin.readline())
function_list = list(map(int, sys.stdin.readline().split()))
Q = int(sys.stdin.readline())
data_list = [list(map(int, input().strip().split())) for _ in range(Q)]
solution(m, function_list, Q, data_list)