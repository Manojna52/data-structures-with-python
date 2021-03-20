x=input().split()
for i in range(0,len(x)):
    x[i]=int(x[i])
x.sort()
a=[0 for i in range(len(x))]
st=0
end=len(x)-1
i=0
for i in range(len(x)):
    if (i+1)%2==0:
        a[i]=x[end]
        end=end-1
    else:
        a[i]=x[st]
        st=st+1
print(a)

        
    
        
