import sys

input = sys.stdin.readline


# 소수 찾기
def find_prime(num):
    # 소수인 수 체크
    prime_check = [True for _ in range(num*2 + 1)]
    # 소수 리스트
    primes = []
    # 순회
    for n in range(2, num*2 + 1):
        # 체크되지 않았다면
        if prime_check[n]:
            # 소수 추가
            primes.append(n)
            # 해당 수의 배수 모두 체크
            for i in range(n, num*2 + 1, n):
                prime_check[i] = False

    return primes


# 이분매칭
def bimatch(idx, connectable, visited, connected):
    # 이미 체크한 수이면
    if visited[idx]:
        return False
    # 체크
    visited[idx] = True
    # 연결될 수 있는 수 목록 순회
    for node in connectable[idx]:
        # 연결될 수 있는 수 이거나 다른 수와 연결할 수 있으면
        if connected[node] < 0 or bimatch(connected[node], connectable, visited, connected):
            # 연결
            connected[node] = idx
            return True
        
    return False


def solution(N, num_list):
    # 리스트에 들어있는 수 중 최대인 수의 두배보다 작은 소수 모두 찾기
    primes = find_prime(max(num_list))
    # 리스트의 각 원소에 더해서 소수가 될 수 있는 원소 인덱스 리스트
    connectable = [[] for _ in range(N)]
    # 리스트 순회
    for i in range(N-1):
        for j in range(i+1, N):
            # 두 수의 합이 소수면
            if num_list[i] + num_list[j] in primes:
                # 각 원소에 더해서 소수가 될 수 있는 원소 인덱스 추가
                connectable[i].append(j)
                connectable[j].append(i)
    # 출력할 결과
    first_connected = []
    # 첫 번째 수와 연결될 수 있는 수로 미리 임의 매칭
    for i in range(len(connectable[0])):
        connected = [-1 for _ in range(N)]
        connected[connectable[0][i]] = 0
        # 순회
        for n in range(N):
            # 방문 리스트
            visited = [False for _ in range(N)]
            # 첫 번째 수는 변경하지 않음
            visited[0] = True
            # 이분매칭
            bimatch(n, connectable, visited, connected)

        # 모든 수가 매칭되면
        if sum([1 for c in connected if c >= 0]) == N:
            # 출력할 수에 추가
            first_connected.append(num_list[connectable[0][i]])

    if first_connected:
        print(*sorted(first_connected))
    else:
        print(-1)        
        

# 입력
N = int(input().strip())
num_list = list(map(int, input().strip().split()))

solution(N, num_list)