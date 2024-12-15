for _ in range(int(input())):
    R, S = input().split()
    string = ''
    for c in list(S):
        for i in range(int(R)):
            string += c
    print(string)