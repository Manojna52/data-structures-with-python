class node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data
class double_linked:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=node(data)
        
        if not self.head:
            self.head=new_node
            new_node.prev=None
            new_node.next=None
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            curr.next=new_node
            new_node.prev=curr
            new_node.next=None
    def prepend(self,data):
        new_node=node(data)
        new_node.next=self.head
        new_node.prev=None
        self.head=new_node
    def a_before(self,value,data):
        new_node=node(data)
        curr=self.head
        prev=self.head
        while(curr.data!=value):
            prev=curr
            curr=curr.next
           
        new_node.next=curr
        prev.next=new_node
        new_node.prev=prev
    def a_after(self,value,data):
        new_node=node(data)
        curr=self.head
        while(curr.data!=value):
            curr=curr.next
        new_node.next=curr.next
        curr.next=new_node
        new_node.prev=curr
    def delete_val(self,value):
        curr=self.head
        prev=self.head
        t=self.head
        while(curr.data!=value):
            prev=curr
            curr=curr.next
            t=curr.next
            
        
        prev.next=t
        
        t.prev=prev.prev
        curr.prev=None
        curr.next=None
    def reverse(self):
        curr=self.head
        temp=None
        vg=self.head
        while(curr):
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
            
        if temp:
            
            self.head=temp.prev
    def check_dup(self):
        cur=self.head
        a=[]
        while(cur):
            if cur.data in a:
                self.delete_val(cur.data)
            a.append(cur.data)
            cur=cur.next
    def sum_pairs(self,sum_value):
        p=self.head
        q=None
        pairs=[]
        while(p):
            q=p.next
            while(q):
                if p.data+q.data==sum_value:
                    pairs.append("("+str(p.data)+","+str(q.data)+")")
                q=q.next
            p=p.next
        print(pairs)
                
    def printv(self):
        curr=self.head
        while(curr):
            
            print(curr.data)
            curr=curr.next
ll=double_linked()
ll.append(7)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(3)
ll.append(2)
ll.check_dup()
ll.printv()
ll.sum_pairs(4)

            
