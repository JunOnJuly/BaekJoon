d = {'black':1, 'brown':10, 'red':100, 'orange':1000, 'yellow':10000, 'green':100000, 'blue':1000000, 'violet':10000000, 'grey':100000000, 'white':1000000000}
r = [input() for _ in range(3)]
print(((len(str(d[r[0]]))-1)*10 + (len(str(d[r[1]]))-1))*d[r[2]])