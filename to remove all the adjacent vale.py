x=input()
a=[]

for i in range(0,len(x)):
    a.append(x[i])
i=1
b=[]
while(i<len(x)):
    if a[i]==a[i-1]:
        b.append(i)
        b.append(i-1)
    i=i+1
str1=''
for i in range(0,len(a)):
    if i not in b:
        str1=str1+a[i]
if str1=='':
    print("no non adjacent")
else:
    print(str1)
   
