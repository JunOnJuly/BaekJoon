def solution(num_list):
    print(sum(num_list)//5)
    print(sorted(num_list)[2])


num_list = [int(input()) for _ in range(5)]
solution(num_list)