class node:
    def __init__(self,data1,data2):
        self.data1=data1
        self.data2=data2
        self.next=None
class linkedlist():
    def __init__(self):
        self.head=None
    def append(data1,data2):
        new_node=node(data1,data2)
        if self.head is None:
            self.head=new_node
            return
        curr=self.head
        while(curr.next):
            curr=curr.next
        curr.next=new_node
    
    def printv(self):
        curr=self.head
        while(curr):
            print(curr.data1,curr.data2)
            curr=curr.next
ll=linkedlist()
ll.append(2,3)
ll.append(4,5)
ll.append(6,7)
ll.printv()
