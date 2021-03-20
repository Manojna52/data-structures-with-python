a=input().split()
b=input().split()
a.extend(b)
for i in range(0,len(a)):
    a[i]=int(a[i])
a=sorted(a)
print(a)
