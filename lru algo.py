x=input().split()
for i in range(len(x)):
    x[i]=int(x[i])
y=input("enter the cache size")
y=int(y)
a=[]
pf=0
check=0
for i in range(len(x)):
    if x[i] not in a:
        pf=pf+1
        if len(a)<y:
            a.append(x[i])
        else:
            a.pop(0)
            a.append(x[i])
    else:
        check=x.index(x[i])
        for j in range(check,len(a)):
            a[j-1]=a[j]
        a.pop()
        a.append(x[i])
print(pf)
            
        
