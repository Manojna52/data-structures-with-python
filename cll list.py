class node:
    def __init__(self,item):
        self.item=item
        self.next=None
class cll:
    def __init__(self):
        self.head=None
    def append(self,item):
        new_node=node(item)
        if not self.head:
            self.head=new_node
            new_node.next=self.head
        else:
            curr=self.head
            while(curr):
                curr=curr.next
                if(curr.next==self.head):
                    break
                
            
            
            curr.next=new_node
            
            
            
            new_node.next=self.head
    def remove(self,value):
        curr=self.head
        prev=curr
        if(value==self.head.item):
            
            self.head=self.head.next
            curr.next=None
            curr=self.head
            while(curr):
                curr=curr.next
                if(curr.next==prev):
                    break
            curr.next=self.head
            
        while(curr):
           
            if(curr.item==value):
                break
            prev=curr
            curr=curr.next
            if(curr.next==self.head):
                print("no element found")
                return
        prev.next=curr.next
        curr.next=None
    def remove_n(self,curr):
        cg=self.head
        prev=self.head
        while(cg!=curr):
            prev=cg
            cg=cg.next
        prev.next=curr.next
        cg.next=None
        
        
            
            
        
    
                
        
    def printv(self):
        curr=self.head
        while(curr):
            print(curr.item)
            curr=curr.next
            if(curr==self.head):
        
                break
    def lent(self):
        curr=self.head
        count=0
        while(curr):
            curr=curr.next
            count=count+1
            if(curr==self.head):
                break
        return count

            
    def josephus(self,value):
        curr=self.head
        while(ll.lent()!=1):
            i=0
                      
           
            while(i!=value):
                print(i)
                curr=curr.next
                i=i+1
            ll.remove_n(curr)
            
                
            
        
        
    
        
           
        
ll=cll()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)


ll.josephus(3)


ll.printv()

            
