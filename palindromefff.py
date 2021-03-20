x=input()
n=len(x)

a=[[0 for i in range(len(x))]for j in range(len(x))]
#all the individual strings are substing
max_lenght=1
i=0
while(i<len(x)):
    a[i][i]=1
    i=i+1
#substring of second element
i=0
start=0
while(i<n-1):
    if(x[i]==x[i+1]):
        a[i][i+1]=1
        start=i
        max_length=2
    i=i+1
k=3
while(k<=n):
    while(i<n-k+1):
        j=i+k-1
        if(a[i+1][j-1] and x[i]==x[j]):
            a[i][j]=1

            if(k>max_length):
                start=i
                max_length=k
        i=i+1
    k=k+1


    
   
        
print(max_length)
        

