import sys

input = sys.stdin.readline


def solution(N, parts):
    # x 기준으로 정렬
    parts = sorted(parts, key=lambda x: x[0])
    # 가장 큰 카운트
    max_cnt = 0
    # 순회
    for i in range(len(parts)-1):
        # 기준 구간
        origin_e = parts[i][1]
        # 구간에 포함되는 수
        cnt = 0
        for j in range(i+1, len(parts)):
            # 비교 구간
            comp_s = parts[j][0]
            comp_e = parts[j][1]
            # 구간에 포함되면
            if comp_e < origin_e:
                cnt += 1
            
            # 구간을 완전히 벗어나면
            elif comp_s > origin_e:
                break
        
        # 최대 카운트 갱신
        max_cnt = max(max_cnt, cnt)
    
    print(max_cnt)


# 입력
N = int(input().strip())
parts = [list(map(int, input().strip().split())) for _ in range(N)]

solution(N, parts)