from collections import Counter
a=Counter(input())
b=Counter(input())
print(a.total()+b.total()-2*(a&b).total())