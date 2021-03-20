class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist():
    def __init__(self):
        self.head=None
    def printv(self):
        curr_node=self.head
        while(curr_node):
            print(curr_node.data)
            curr_node=curr_node.next
    def append(self,data):
        new_node=node(data)
        
        if self.head is None:
           
            self.head=new_node
            return
        last_node=self.head
        while(last_node.next):
            last_node=last_node.next
        
        last_node.next=new_node
    def add_first(self,data):
        new_node=node(data)
        
        
        new_node.next=self.head
        self.head=new_node
    def add_after(self,data,vals):
        new_node=node(data)
        curr_node=self.head
        while(curr_node.data!=vals):
            curr_node=curr_node.next
        new_node.next=curr_node.next
        curr_node.next=new_node
        

        
        
             
        
        
        
ll=linkedlist()
ll.append("3")
ll.append("4")
ll.add_first("6")
ll.add_first("5")
ll.add_after("9","4")
ll.printv()

