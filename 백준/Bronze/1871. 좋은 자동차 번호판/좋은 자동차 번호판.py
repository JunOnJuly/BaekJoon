for _ in range(int(input())):
    a,b=input().split('-')
    if abs(sum([(26**i)*(ord(a[2-i])-ord('A')) for i in range(3)])-int(b))<=100:
        print('nice')
    else:
        print('not nice')