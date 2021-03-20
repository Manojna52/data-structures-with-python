class stack():
    def __init__(self):
        self.item=[]
    def push(self,item):
        self.item.append(item)
    def pop(self):
        self.item.pop()
    def display(self):
        print(self.item)
s=stack()
s.push("a")
s.push(3)
s.push(4)
s.display()
s.pop()
s.pop()
s.display()
