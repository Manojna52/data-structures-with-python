class node:
    def __init__(self,item):
        self.item=item
        self.next=None
class linked_list():
    def __init__(self):
        self.head=None
    def append(self,item):
        new_node=node(item)
        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=new_node
    def printv(self):
        curr=self.head
        while(curr!=None):
            print(curr.item)
            curr=curr.next
    def append_first(self,item):
        new_node=node(item)
        new_node.next=self.head
        self.head=new_node
        
        
            
ll=linked_list()
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append_first(4)
ll.append_first(8)
ll.printv()
        
