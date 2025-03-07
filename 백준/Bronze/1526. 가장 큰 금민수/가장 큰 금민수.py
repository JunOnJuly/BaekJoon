for n in range(int(input()),3,-1):
    if all(map(lambda x:x=='4'or x=='7',str(n))):
        print(n)
        break