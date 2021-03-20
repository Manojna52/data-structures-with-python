#good or bad string
x=input()
a=['a','e','i','o','u']
cons=0
vow=0
for i in range(0,len(x)):
    if x[i] in a:
        vow=vow+1
        cons=0
        if(vow>5):
            print("yes")
            break
        
    elif x[i]=='?':
        vow=vow+1
        cons=cons+1
        if(vow>5 or cons>3):
            print("yes")
    else:
        cons=cons+1
        vow=0
        if(cons>3):
            print("yes")
