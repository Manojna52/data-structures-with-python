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
    def swap(self,item1,item2):
        ptr1=self.head
        ptr2=self.head
        while(ptr1.data!=item1):
            ptr1=ptr1.next
        while(ptr2.data!=item2):
            ptr2=ptr2.next
        ptr1.data,ptr2.data=ptr2.data,ptr1.data
    def rotate(self,item):
        p=self.head
        q=self.head
        while(q.data!=item):
            q=q.next
            p=p.next
        while(q.next!=None):
            q=q.next
        q.next=self.head
        self.head=p.next
        p.next=None
        
        
    
    def merged_list(self,ll):
        p=self.head
        q=ll.head
        s=None
        if(p==None):
            pass
           
        if(q==None):
            pass

        if p and q:
            if(p.data>=q.data):
                s=q
                q=s.next
            else:
                s=p
                p=s.next
            new_head=s
        while(p and q):
            if(p.data>=q.data):
                s.next=q
                s=q
                q=s.next
            else:
                s.next=p
                s=p
                p=s.next
        if not p:
            s.next=q
        if not q:
            s.next=p
        return new_head
        

        
        
        
            
        
list1=linkedlist()
list1.append("1")
list1.append("2")
list1.append("3")
list1.append("4")
list1.append("5")
list1.append("6")
list1.rotate("4")
list1.printv()

