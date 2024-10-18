import sys

input = sys.stdin.readline


# 이분매칭
def bimatch(idx, connectable, connected, visited):
    # 이미 방문했으면 패스
    if visited[idx]:
        return False
    
    # 방문 체크
    visited[idx] = True
    # 순회
    for node in connectable[idx]:
        # 만날 수 있거나 뺏을 수 있으면
        if connected[node] < 0 or bimatch(connected[node], connectable, connected, visited):
            # 만나기
            connected[node] = idx

            return True
    
    return False


def solution(N, people):
    # 남자 리스트 / 여자 리스트
    males = []
    females = []
    # 순회
    for h, s, m, sp in people:
        # 남자면
        if s == 'M':
            males.append([int(h), m, sp])
        # 여자면
        else:
            females.append([int(h), m, sp])

    # 만날 수 있는 목록 (남자 -> 여자)
    connectable = [[] for _ in range(len(males))]
    # 남자
    for m in range(len(males)):
        mh, mm, msp = males[m]
        # 여자
        for f in range(len(females)):
            fh, fm, fsp = females[f]
            # 만날 수 있으면
            if all([abs(mh-fh) <= 40, mm==fm, msp!=fsp]):
                connectable[m].append(f)
    
    # 연결된 목록
    connected = [-1 for _ in range(len(females))]
    # 순회
    for idx in range(len(males)):
        # 방문 목록
        visited = [False for _ in range(len(males))]
        # 이분매칭
        bimatch(idx, connectable, connected, visited)

    # 남자는 모두 가고
    # 만날 가능성이 있는 여자는 빼기
    print(len(males) + len(females) - sum([1 for c in connected if c >= 0]))


# 입력
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    people = [list(input().strip().split()) for _ in range(N)]

    solution(N, people)