x=input().split()
for i in range(0,len(x)):
    x[i]=int(x[i])
a=[0 for i in range(len(x))]
for i in range(0,len(x)):
    g=max(x[i:])
    if(g>x[i]):
        a[i]=g
    else:
        a[i]=-1

print(a)
