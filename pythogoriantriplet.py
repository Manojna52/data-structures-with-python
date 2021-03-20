x=input()
x=int(x)
c,m=0,2
for n in range(1,m):
    a=m*m-n*n
    b=2*n*m
    c=m*m+n*n
    while(c>x):
        break
        
    print(a,b,c)
    m=m+1
    print(m)
