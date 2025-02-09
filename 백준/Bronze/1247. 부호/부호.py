for _ in range(3):
    print((lambda x: 0 if not x else '+' if x>0 else '-')(sum([int(input()) for _ in range(int(input()))])))