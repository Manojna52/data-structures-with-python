class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data:
            if(data<self.data):
                if(self.left is None):
                    self.left=node(data)
                else:
                    self.left.insert(data)
            if(data>self.data):
                if(self.right is None):
                    self.right=node(data)
                else:
                    self.right.insert(data)
            
                
            
            
        else:
            self.data=data
    def printin(self,key):
        if(self.left):
            self.left.printin(key)
        print(self.data)
        
        if self.right:
            self.right.printin(key)
    def finddev(self,value):
        
        
        if(self.left):
            self.left.finddev(value)
        if self.data==value:
            print(self.right.data)
        
        
            
            
        if self.right:
            self.right.finddev(value)
        
    def preprint(self):
        print(self.data)
        if self.left:
            self.left.preprint()
        if self.right:
            self.right.preprint()
    def postprint(self):
        if(self.left):
            self.left.postprint()
        if self.right:
            self.right.postprint()
        print(self.data)
va=node(10)
va.insert(1)
va.insert(2)
va.insert(5)
va.insert(3)
va.insert(7)
va.insert(11)
va.insert(19)
va.insert(20)
print("pre order")
va.preprint()
print("post order")
va.postprint()
print("inorder")
va.printin(2)
va.finddev(2)



