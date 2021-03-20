a=input().split()
for i in range(0,len(a)):
    a[i]=int(a[i])
max_end,max_sof=0,0
for i in range(0,len(a)):
    max_end=max_end+a[i]
   
    if(max_sof<max_end):
        max_sof=max_end

    if(max_end<0):
       max_end=0
print(max_sof)
