import sys

input = sys.stdin.readline


def solution(x, y, c):
    # 가능한 수의 범위
    n_range = [0, min(x, y)]
    # 순회
    while True:
        # 수 고르기
        z = sum(n_range) / 2
        # 왼쪽 빌딩 높이
        a = pow(pow(x, 2) - pow(z, 2), 1/2)
        # 오른쪽 빌딩 높이
        b = pow(pow(y, 2) - pow(z, 2), 1/2)
        # 계산된 교차하는 y 의 높이
        C = round((a*b) / (a+b), 6)
        # 계산 높이가 더 높으면
        if C > c:
            # 계산 높이가 낮아져야 하므로 z 값 늘이기
            n_range[0] = z
        
        # 계산 높이가 더 낮으면
        elif C < c:
            # 계산 높이가 높아져야 하므로 z 값 줄이기
            n_range[1] = z

        # 같으면
        else:
            # 출력
            print(f'{z:.3f}')
            break


x, y, c = map(float, input().split())
solution(x, y, c)