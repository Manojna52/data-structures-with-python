class stack:
    def __init__(self):
        self.name=[]
    def push(self,item):
        self.name.append(item)
    def pop(self):
        print(self.name.pop(),end='')
    def printv(self):
        print(self.name)
s=stack()
x=input()
   
for i in range(0,len(x)):
    print(x[i])
    s.push(x[i])
s.printv()
for i in range(0,len(x)):
    s.pop()
               

        
