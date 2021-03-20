from collections import Counter
x=input().split()
for i in range(0,len(x)):
    x[i]=int(x[i])
a=Counter(x)
x.sort()
x=sorted(x,key=a.get)
print(x)
