#longest common subsequence
x=input()
y=input()
a=[]
b=[]
for i in range(0,len(x)):
    a.append(x[i])
for i in range(0,len(y)):
    b.append(y[i])
    
i=len(x)-1
j=len(y)-1
def check(a,b,i,j):
    if i<=0 or j<=0:
        return
    if x[i]==y[j]:
        return check(a,b,i-1,j-1)
    if x[i]!=y[j]:
        return max(check(a,b,i-1,j),check(a,b,i,j-1))
print(check(x,y,i,j))


    
