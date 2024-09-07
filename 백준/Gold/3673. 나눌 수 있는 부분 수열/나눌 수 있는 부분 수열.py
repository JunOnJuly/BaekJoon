import sys
from collections import Counter

input = sys.stdin.readline


def solution(d, n, data_list):
    # 결과
    result = 0
    # 누적합 리스트
    subsum = [0] + data_list[:]
    for i in range(1, n+1):
        subsum[i] += subsum[i-1]
        # 미리 나누기
        subsum[i] %= d
    # 같은 나머지를 가진 수 카운터
    subsum_counter = Counter(subsum)
    # 같은 나머지를 가진 수 끼리 빼면 d 로 나누어떨어짐
    # 큰 수에서 작은수를 빼야 하므로
    # 빼서 d 로 나누어떨어지는 수의 쌍은
    # (k)(k-1)/2 , k 는 해당 나머지를 가진 수의 개수
    for key, value in subsum_counter.items():
        # 한 개 뿐이면 세지 않음
        result += value*(value-1)//2

    return result


# 입력
c = int(input().strip())
for _ in range(c):
    d, n = map(int, input().strip().split())
    data_list = list(map(int, input().strip().split()))
    print(solution(d, n, data_list))