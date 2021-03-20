#revison of sum of four
x=input().split()
for i in range(0,len(x)):
    x[i]=int(x[i])
mp=dict()
for i in range(0,len(x)):
    for j in range(i,len(x)):
        mp[x[i]+x[j]]=[i,j]
print(mp)
