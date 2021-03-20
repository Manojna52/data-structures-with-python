class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printv(self):
        curr_node=self.head
        while(curr_node):
            print(curr_node.data)
            curr_node=curr_node.next
            
    def append(self,item):
        new_node=node(item)
        if(self.head==None):
            self.head=new_node
            return
        curr_node=self.head
        while(curr_node.next):
            curr_node=curr_node.next
        curr_node.next=new_node
    def add_first(self,item):
        new_node=node(item)
        
        new_node.next=self.head
        self.head=new_node
    def add_after(self,item,vale):
        new_node=node(item)
        vale=self.head
        new_node.next=vale.next
        vale.next=new_node
ll=linkedlist()
ll.append("3")
ll.append("4")
ll.append("7")
ll.add_first("2")
ll.add_first("9")
ll.add_after("8","3")

ll.printv()
        
        
