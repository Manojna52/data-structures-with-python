x=input()
y=input()
result=0
a=[[0 for i in range(len(y)+1)]for j in range(len(x)+1)]
for i in range(len(x)+1):
    for j in range(len(y)+1):
        if i==0 or j==0:
            a[i][j]=0
        elif x[i-1]==y[j-1]:
            a[i][j]=max(a[i-1][j],a[i][j-1])
        else:
            a[i][j]=a[i-1][j-1]+1
            result=max(result,a[i][j])
print(result)
