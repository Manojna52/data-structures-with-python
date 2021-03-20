def formatproduct(A,B):
    x=int(A)
    y=int(B)
    val1=1
    for i in range(x,y+1):
        val1=val1*i
    count=0
    r=0
    ac=''
    while(val1!=0):
        r=val1%10
        if r==0:
            count=count+1
            val1=val1//10
        else:
            break
    if len(str(val1))<=10:
        ac=ac+str(val1)+"*"+"10"+"^"+str(count)
        return ac
    else:
        val1=str(val1)
        c1=val1[:5]
        c2=val1[len(val1)-5:]
        ac=ac+c1+"..."+c2+"*"+"10"+"^"+str(count)
        return ac
        
print(formatproduct(411,414))

    
    
