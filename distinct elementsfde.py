from collections import Counter
x=input().split()
for i in range(len(x)):
    x[i]=int(x[i])
y=input()
y=int(y)
k=0
while(True):
    if k+y>len(x):
        break
    
    
    print(len(Counter(x[k:k+y])))
    k=k+1
    
        
    
    
