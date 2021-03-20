#practice minimum inserton to convert it in palindrome
x=input()
i=0
j=len(x)-1

def palin(i,j):
    if(i>j):
        return 10000000
    if(i==j):
        return 0
    if x[i]==x[j]:
        return palin(i+1,j-1)
    if x[i]!=x[j]:
        return 1+min(palin(i+1,j),palin(i,j-1))
print(palin(i,j))
