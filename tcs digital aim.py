x=input()
a=[]
val=''
count=0
t=[]
ty=[]
for i in range(0,len(x)):
    a.append(x[i])

for i in range(0,len(a)):
    if a[i]=='(':
        
        if ty==[]:
            ty.append(')')
            
        else:
            ty.append(')')
            count=0
        
    else:
        if ty!=[]:
            val=ty[-1]
        
            ty.pop()
            
        
        
        
            if val==')':
            
                count=count+1
                t.append(count)
print(2*max(t))



        
        
