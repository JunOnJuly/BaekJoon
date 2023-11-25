import sys
from collections import defaultdict


def solution(K, L, data_list):
    # 수강 대기 목록 사전
    wait_dict = defaultdict(int)
    # 사전 최신화
    for idx, data in enumerate(data_list):
        wait_dict[data] = idx
    # 사전 정렬
    wait_dict_list = sorted(wait_dict.items(), key=lambda x:x[1])
    # 출력
    for idx, (key, value) in enumerate(wait_dict_list):
        if idx == K:
            break
        print(key.strip())


K, L = map(int, sys.stdin.readline().split())
data_list = [sys.stdin.readline() for _ in range(L)]
solution(K, L, data_list)