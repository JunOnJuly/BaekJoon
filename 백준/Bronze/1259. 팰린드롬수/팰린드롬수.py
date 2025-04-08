while (n:=int(input())):
    n=str(n)
    print('yes'if n==n[::-1] else 'no')