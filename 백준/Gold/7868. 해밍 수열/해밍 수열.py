import sys
import heapq as hq
input = sys.stdin.readline


def solution(p1, p2, p3, i):
    # 곱해질 수
    muls = sorted([p1, p2, p3])
    # 최소힙
    q = [p1, p2, p3]
    hq.heapify(q)
    # 삽입된 수 목록
    ns = set(q)
    # 카운트
    cnt = 0
    # 순회
    while i-cnt:
        # 가장 작은 수
        n = hq.heappop(q)
        # 카운트 + 1
        cnt += 1
        # 가장 작은 수에 곱해질 수 곱하기
        for m in muls:
            # 곱해진 수
            nm = n * m
            # 존재하지 않으면 최소힙에 삽입
            if nm not in ns:
                hq.heappush(q, n*m)
                # 목록 체크
                ns.add(nm)
    
    print(n)


p1, p2, p3, i = map(int, input().split())
solution(p1, p2, p3, i)