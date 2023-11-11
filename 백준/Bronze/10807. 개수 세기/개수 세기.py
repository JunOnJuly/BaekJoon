def solution(data_list, v):
    return data_list.count(v)
    
    
N = int(input())
data_list = list(map(int, input().split()))
v = int(input())
print(solution(data_list, v))