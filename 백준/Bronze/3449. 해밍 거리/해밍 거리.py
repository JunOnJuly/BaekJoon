for _ in range(int(input())):
    print(f'Hamming distance is {sum([c!=C for c, C in zip(input(), input())])}.')