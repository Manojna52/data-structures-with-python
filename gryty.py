x=input()
y=input()
min1=len(x)
t=len(y)
for i in range(0,len(y)):
    if y[i] in x:
        t=x.index(y[i])
    if t<min1:
        min1=t
print(x[min1])

    
    
