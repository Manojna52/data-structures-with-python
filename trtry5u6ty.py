x=input().split()
for i in range(len(x)):
    x[i]=int(x[i])
y=input()
y=int(y)
i=0
j=0

sum1=0
sum1=sum1+x[0]
while(True):
   
    if sum1<y:
        sum1=sum1+x[j]
        j=j+1
        
        
        
    if sum1>y:
        sum1=sum1-x[i]
        i=i+1
        sum1=sum1-x[i]
    if i>=j:
        print("found not")
        break
    if sum1==y:
        print("found")
        break
print(x[i:j+1])
