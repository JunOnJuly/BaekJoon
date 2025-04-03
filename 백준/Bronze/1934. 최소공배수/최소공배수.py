from math import lcm
from functools import reduce
for i in range(int(input())):
    print(reduce(lcm,map(int,input().split())))