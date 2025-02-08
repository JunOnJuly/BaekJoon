for _ in range(int(input())):
    print(f'${sum([x*y for x,y in zip(list(map(int, input().split())), [350.34, 230.90, 190.55, 125.30, 180.90])]):.2f}')