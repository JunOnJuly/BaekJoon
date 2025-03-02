c=0
for i in range(int(input())+1):
    if not i:
        continue
    while True:
        if not i%5:
            c+=1
            i//=5
        else:
            break
print(c)