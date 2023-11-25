import sys
from collections import defaultdict


def solution(n, data_list):
    # 출입 명부 딕셔너리
    in_out_dict = defaultdict(int)
    # 순회하면서 상태 최신화
    for name, state in data_list:
        if state == 'enter':
            in_out_dict[name] = 1
        else:
            in_out_dict[name] = 0
    # 딕셔너리 정렬
    in_out_dict = dict(sorted(in_out_dict.items(), reverse=True))
    # 순회하며 출력
    for key, value in in_out_dict.items():
        if value:
            print(key)    


n = int(input())
data_list = [sys.stdin.readline().strip().split(' ') for _ in range(n)]
solution(n, data_list)