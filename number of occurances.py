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
    def append(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while(last_node.next):
            last_node=last_node.next
        
        last_node.next=new_node
        
       
    def add_first(self,item):
        new_node=node(item)
        
        new_node.next=self.head
        self.head=new_node
    def add_after(self,item,vale):
        new_node=node(item)
        vale=self.head
        new_node.next=vale.next
        vale.next=new_node
    def count(self):
        cur=self.head
        count=0
        while(cur!=None):
            cur=cur.next
            count=count+1
        return count
    def find_back(self,pos):
        length=self.count()
        
        cur=self.head
        prev=self.head
        i=length-pos
        j=0
        while(i!=j):
            prev=cur
            cur=cur.next
            j=j+1
        print(cur.data)
    def occurances(self,value):
        count=0
        cur=self.head
        while(cur):
           
            if(cur.data==value):
                
                count=count+1
            cur=cur.next
        print("the number of occurances of",value,"is",count)
ll=linkedlist()
ll.append("3")
ll.append("4")
ll.append("7")
ll.add_first("2")
ll.add_first("9")
ll.add_after("8","3")
ll.append("1")
ll.append("1")
ll.append("1")
ll.append("1")

ll.printv()
print("element from last")
ll.find_back(4)
ll.occurances("1")

        
        
