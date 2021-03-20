class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist():
    def __init__(self):
        self.head=None
    def append(self,item):
        new_node=node(item)
        if self.head is None:
            self.head=new_node
        else:
            prev=self.head
            while(prev.next):
                prev=prev.next
            prev.next=new_node
    def printv(self):
        curr=self.head
        while(curr):
            print(curr.data)
            curr=curr.next
    def attach(self):
        prev=self.head
        while(prev.next):
            prev=prev.next
        prev.next=ll.head.next.next.next
    def check_inter(self,l_2):
        mp=dict()
        curr=self.head
        prev=l_2.head
        t=0
        while(curr):
            t=hash(curr)
            t=t%1000
            mp[t]=1
            curr=curr.next
        while(prev):
            t=hash(prev)
            t=t%1000
            if t in mp:
                print("intersection found")
                print(prev.data)
                break
            prev=prev.next
    def form(self):
        prev=self.head
        while(prev.next):
            prev=prev.next
        prev.next=self.head.next.next.next
        
    def to_check(self):
        prev=self.head
        mp=dict()
        flag=0
        curr=None
        y=None
        while(prev):
            y=curr
            curr=prev
            
            t=hash(prev)
            t=t%1000
            print(t)
            
            if t in mp:
                flag=1
                print("found")
                break
            else:
                mp[t]=1
            prev=prev.next
        print(curr.data)
        print(prev.data)
        y.next=None
        
        if(flag==0):
            print("no loop")
        else:
            pass
    def lengtha(self):
        curr=self.head
        count=0
        while(curr):
            curr=curr.next
            count=count+1
        return count
    def rev(self):
        prev=None
        next1=None
        curr=self.head
        while(curr!=None):
            next1=curr.next
            curr.next=prev
            prev=curr
            curr=next1
        self.head=prev
        
        
        
      
    
                        
                    
                    
                    
           
                
                
        
ll=linkedlist()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

ll.printv()
ll.rev()
ll.printv()



            
