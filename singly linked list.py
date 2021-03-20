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
    def delete_f(self):
        curr_node=self.head
        self.head =curr_node.next
        curr_node.next=None
    def delete_pos(self,pos):
        curr_node=self.head
        prev_node=self.head
        i=0
        
        while(i!=pos-1):
            i=i+1
            prev_node=curr_node
            curr_node=curr_node.next
            
       
        prev_node.next=curr_node.next
        curr_node.next=None
    def delete_last(self):
        curr_node=self.head
        prev_node=self.head
        while(curr_node.next!=None):
            prev_node=curr_node
            
            curr_node=curr_node.next
        prev_node.next=None
    def length_node(self):
        count=0
        curr_node=self.head
        if(curr_node==None):
            print("it is empty and the lenth is zero")
            
        else:
           while(curr_node!=None):
               curr_node=curr_node.next
               count=count+1
        print("the length is",count)
        return count
    def swap(self,item1,item2):
        ptr1=self.head
        ptr2=self.head
        while(ptr1.data!=item1):
            ptr1=ptr1.next
        while(ptr2.data!=item2):
            ptr2=ptr2.next
        ptr1.data,ptr2.data=ptr2.data,ptr1.data
    def middle_ele(self):
        l=self.length_node()
        l=(l+1)//2
        i=0
        prev=self.head
        while(i!=l-1):
            prev=prev.next
            i=i+1
        print(prev.data)
    def rotate(self,item):
        p=self.head
        q=self.head
        i=0
        while(q.next):
            if i <item-1:
                p=p.next
                q=q.next
                i=i+1
            else:
                q=q.next
        
        q.next=self.head
        self.head=p.next
        p.next=None
        
        
        
            
        
ll=linkedlist()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
ll.append(8)
ll.printv()
ll.middle_ele()
ll.rotate(4)
print("the value is")
ll.printv()
ll.rotate(4)
ll.printv()



