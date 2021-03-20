#thr subarray equivalent to sum
a=input().split()
for i in range(0,len(a)):
    a[i]=int(a[i])
y=input()
y=int(y)
i=0
j=0
sum1=0
while(True):
    if sum1==y:
        break
    if sum1<y:
        sum1=sum1+a[j]
        j=j+1
    if sum1>y:
        sum1=sum1-a[i]
        i=i+1
print(a[i:j])
