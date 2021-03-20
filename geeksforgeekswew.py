x=input().split()
for i in range(len(x)):
    x[i]=int(x[i])
a=[0 for i in range(len(x))]
a[0]=x[0]*x[1]
i=1
k=1
while(k<len(a)-1):
    a[i]=x[i-1]*x[i+1]
    k=k+1
    i=i+1
a[k]=x[k]*x[k-1]
print(a)
    
    
