x=input().split()
for i in range(len(x)):
    x[i]=int(x[i])
a=[1 for i in range(len(x))]
b=[0 for i in range(len(x))]
for i in range(1,len(x)):
    t=[]
    for j in range(0,i+1):
        if(x[i]>x[j] and a[i]<a[j]+1):
            a[i]=a[j]+1
            t.append(x[j])
    print(t)
            
            
print(a)

