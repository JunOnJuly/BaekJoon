for _ in range(int(input())):
    n=int(input())
    m=n
    while n!=1:
        if n%2:
            n=3*n+1
        else:
            n//=2
        m=max(m,n)
    print(m)