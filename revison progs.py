#sort array according to frequency
from collections import Counter
x=input().split()
x.sort()
count=Counter(x)

new_list=sorted(x,key=count.get,reverse=True)
print(new_list)
