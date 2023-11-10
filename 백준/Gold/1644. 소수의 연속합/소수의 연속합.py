def solution(N):
    # 소수 리스트 만들기
    # 0 은 누적합 만들기 쉽게 하려고 붙임
    prime_list = [0] + find_prime(N)
    # 소수 리스트 누적합 리스트 만들기
    subsum_prime = make_subsum(prime_list)
    # 투포인터
    start = 0
    end = 1
    # 경우의 수
    cnt = 0 
    while True:
        # end 가 인덱스를 넘어가면 끝
        if end >= len(subsum_prime):
            return cnt
        # 포인터 값
        start_value = subsum_prime[start]
        end_value = subsum_prime[end]
        # 구간 합
        subsum = end_value - start_value
        # 구간 합이 목표치보다 작으면 end + 1
        if subsum < N:
            end += 1
            continue
        # 구간 합이 목표치보다 크면 start + 1
        elif subsum > N:
            start += 1
            continue
        # 같으면 경우의 수 + 1, end + 1
        else:
            cnt += 1
            end += 1
            continue


# 소수 리스트를 만드는 함수
def find_prime(N):
    # 소수 리스트
    prime_list = [2]
    # 3 부터 2 씩 증가하면서 순회
    for num in range(3, N+1, 2):
        # 소수로 나누어떨어지면 소수가 아님
        for prime in prime_list:
            # 나누어 떨어지면 다음 수            
            if not num%prime:
                break
            # 목적수의 제곱근보다 크면 종료
            if prime > num**(1/2):
                prime_list.append(num)
                break
    return prime_list


# 누적합 리스트를 만드는 함수
def make_subsum(prime_list):
    # 순회
    for idx in range(1, len(prime_list)):
        prime_list[idx] += prime_list[idx-1]
    return prime_list


N = int(input())
print(solution(N))