x=input()
check=0
min1=0
a=[]
for i in range(len(x)):
    if x[i] in a:
        a=[]
        
        if check>min1:
            min1=check
            check=0
    else:
        a.append(x[i])
        check=check+1
print(min1)
