#dll
class node:
    def __init__(self,item):
        self.item=item
        self.next=None
        self.prev=None
class dll():
    def __init__(self):
        self.head=None
    def append(self,item):
        new_node=node(item)
        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            
            while(curr.next):
                curr=curr.next
            curr.next=new_node
            new_node.prev=curr
            
    def printv(self):
        curr=self.head
        
        while(curr):
            print(curr.item)
            
            curr=curr.next
ll=dll()
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(7)
ll.printv()
            
            
    
