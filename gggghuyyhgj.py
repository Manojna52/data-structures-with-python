class stack():
    def __init__(self):
        self.item=[]
    def push(self,item):
        self.item.append(item)
    def pop(self):
        self.item.pop()
    def check_disp():
        print(self.item)
    def check_emp(self):
        if(self.item==[]):
            return 0
        else:
            return 1
def is_match(p1,p2):
    if(p1=='(' and p2==')'):
        return 1
    elif(p1=='[' and p2==']'):
        return 1
    elif(p1=='(' and p2==')'):
       return 1
    else:
         return 0
    
def check(x):
    flag=0
    
    i=0
    while(i<len(x)):
        i=i+1
        y=x[i]
        if y in '([{':
            s.push(y)
        else:
            k=s.check_emp()
            if(k==0):
                flag=0
                break
            else:
                t=s.pop()
                u=is_match(y,t)
                if u==0:
                    flag=0
                    break
                else:
                    flag=1
flag=0        
s=stack()

r=input()
check(r)
if(flag==0):
    print("not balanced")
else:
    print("balanced")
                        
                        
        
        
            
            
