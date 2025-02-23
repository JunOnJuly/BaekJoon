while True:
    s=input()
    if s=='#':
        break
    print(len(set(map(lambda x:x.isalpha()*x.lower(), list(s)))-set([''])))