def solution(N, score_list):
    # 최댓값 
    M = max(score_list)
    # 현재 평균
    now_mean = sum(score_list)/len(score_list)
    # 새로운 평균을 계산
    new_mean = now_mean/M*100
    print(new_mean)


N = int(input())
score_list = list(map(int, input().split()))
solution(N, score_list)