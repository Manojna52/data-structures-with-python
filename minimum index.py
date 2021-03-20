x=input().split()
for i in range(0,len(x)):
    x[i]=int(x[i])
y=input()
y=int(y)
z=input()
z=int(z)
x_i=-1
y_i=-1
diff=1000000000

for i in range(0,len(x)):
    if x[i]==y:
        x_i=i+1
    if x[i]==z:
        y_i=i+1
    if x_i!=-1 and y_i!=-1:
        diff=min(diff,abs(x_i-y_i))
if x_i==-1 or y_i==-1:
    print("-1")
else:
    print(diff)

        
