import sys

input = sys.stdin.readline


def solution(N):
    # N 이하의 소수 목록
    uniques = find_uniques(N)
    # 결과
    result = 1
    # N 이하의 소수들의 제곱수들 중 N 보다 작은 가장 큰 수
    for unique in uniques:
        # 가장 큰 수
        max_num = unique
        while max_num <= N:
            max_num *= unique
        
        # 한 번 나누기
        max_num //= unique
        # 결과에 곱하기
        result *= max_num
    
    print(result%987654321)
    

# N 이하의 소수를 모두 구하는 함수
def find_uniques(N):
    # 소수 목록
    uniques = []
    # 소수 판정 리스트
    is_unique = [0, 0] + [1 for _ in range(N-1)]
    # 순회
    for i in range(2, len(is_unique)):
        # 소수면
        if is_unique[i]:
            # 소수 목록 추가
            uniques.append(i)
            # 배수 모두 소수 아님 체크
            for j in range(2*i, len(is_unique), i):
                is_unique[j] = 0

    return uniques


N = int(input())
solution(N)