x=input().split()
for i in range(0,len(x)):
    x[i]=int(x[i])
y=input()
y=int(y)
sum1=0
i=0
j=0
while(i>=j):
    if sum1<y:
    
        
        sum1=sum1+x[i]
        i=i+1
        
    if sum1>y:
        
        sum1=sum1-x[j]
        j=j+1
        
    if sum1==y:
        print(x[j:i+1])
        break
        
        
