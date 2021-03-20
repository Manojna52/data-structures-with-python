#kedens algorith
x=input().split()
for i in range(0,len(x)):
    x[i]=int(x[i])
meh=0
msf=0
for i in range(0,len(x)):
    meh=meh+x[i]
    if(meh<0):
        meh=0
    if msf<meh:
        msf=meh
print(msf)
