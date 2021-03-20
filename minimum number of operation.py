x=input()
x=int(x)
def target(x):
    if(x==0):
        return 0;
    if(x%2==0):
        return 1+target(x//2);
    if(x%2!=0):
        return 1+target(x-1);
print(target(x))
