class node:
    def __init__(self,item):
        self.item=item
        self.next=None
class cll():
    def __init__(self):
        self.head=None
    def append(self,item):
        new_node=node(item)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            curr=self.head
            while(curr):
                curr=curr.next
                if curr.next==self.head:
                    break
            curr.next=new_node
            new_node.next=self.head
    def printv(self):
        curr=self.head
        
        while(curr):
            print(curr.item)
            curr=curr.next
ll=cll()
ll.append(2)
ll.append(5)
ll.append(7)
ll.append(9)
ll.printv()
            
            
