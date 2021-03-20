def left_side(A,val,ind):
    min1=val
    count=0
    for i in range(ind,-1,-1):
        if min1>A[i]:
            
            count=count+1
    return count
    

def right_side(A,val,ind):
    min1=val
    count1=0
    for i in range(ind,len(A)):
        if min1>A[i]:
        
            count1=count1+1
    return count1
def value(A):
    min3=0
    res=0
    for i in range(0,len(A)):
        val1=left_side(A,A[i],i)
        val2=right_side(A,A[i],i)
        
        res=(val1+val2)*i+1
        if min3<res:
            min3=res
    return res
A=[5,1,2,4,1]
print(value(A))

        
        
    
            
    
