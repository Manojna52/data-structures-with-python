#longest increasing sub
x=input().split()
for i in range(0,len(x)):
    x[i]=int(x[i])

a=[1 for i in range(len(x))]
for i in range(1,len(x)):
    for j in range(0,i+1):
        
        if(x[i]>x[j] and a[i]<=a[j]):
            a[i]=a[j]+1
            print(a)
            
            
           
