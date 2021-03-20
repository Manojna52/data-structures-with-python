class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist():
    def __init__(self):
        self.head=None
    def append(self,data):
        Node=node(data)
        if self.head is None:
            self.head=Node
            return
        else:
            p=self.head
            while(p.next!=None):
                p=p.next
            p.next=Node
            
    def display(self):
        t=self.head
        while(t !=None):
            print(t.data)
            t=t.next
y=linkedlist()
y.append("3")
y.append("5")
y.append("6")
y.display()
            
            
