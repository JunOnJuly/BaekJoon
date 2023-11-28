import sys
from collections import defaultdict


def solution(S, data_list):
    # 문자별 누적합
    subsum = [[0 for _ in range(len(S)+1)] for __ in range(26)]
    # 문자열 순회 및 누적합 리스트 완성
    for idx_S in range(len(S)):
        for idx_subsum in range(len(subsum)):
            # 해당 문자면 해당 문자 누적합의 해당 인덱스 값 + 1
            if idx_subsum == ord(S[idx_S])-97:
                subsum[idx_subsum][idx_S+1] = subsum[idx_subsum][idx_S] + 1
            # 아니면 그대로
            else:
                subsum[idx_subsum][idx_S+1] = subsum[idx_subsum][idx_S]
    # 데이터 순회 
    for now_str, start, end in data_list:
        print(subsum[ord(now_str)-97][int(end)+1] - subsum[ord(now_str)-97][int(start)])
                
        
S = sys.stdin.readline().strip()
q = int(sys.stdin.readline().strip())
data_list = [sys.stdin.readline().strip().split() for _ in range(q)]
solution(S, data_list)