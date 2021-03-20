from collections import Counter
x=input()
a=[]
for i in range(0,len(x)):
    a.append(x[i])
prev=''

flag=0
t=[]
while(a!=[]):
    val=Counter(a)
    a=sorted(a,key=val.get,reverse=True)
    if a[0]==prev:
        flag=0
        for i in range(0,len(a)):
            if a[i]!=prev:
                flag=1
                break
        if flag==1:
            prev=a[i]
            t.append(a[i])
            a.pop(i)
        else:
            break
    else:
        t.append(a[0])
        prev=a[0]
        
        a.pop(0)
if len(t)!=len(x):
    print("Impossible")
else:
    print("".join(t))

    
            
        
    
    
    
    
    


             

