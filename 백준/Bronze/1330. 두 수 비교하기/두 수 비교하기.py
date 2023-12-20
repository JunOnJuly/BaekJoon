def solution(A, B):
    if A > B:
        print('>')
    elif A < B:
        print('<')
    else:
        print('==')
    
    
A, B = map(int, input().split())
solution(A, B)