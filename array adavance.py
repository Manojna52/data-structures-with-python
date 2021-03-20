x=input().split()
a=[0]*len(x)
u=0
for i in range(0,len(x)):
    i=u
    
    a=x[i:i+i]
    g=max(a)
    u=x.index(g)
if(u==len(x)-1):
    print("yes")
else:
    print("no")
    
    
    
