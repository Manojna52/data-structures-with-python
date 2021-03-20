class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist():
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=node(data)
        cur=self.head
        if(cur==None):
            self.head=new_node
            return
        else:
            cur=self.head
            while(cur.next):
                cur=cur.next
            cur.next=new_node
    def printv(self):
        curr=self.head
        while(curr):
            print(curr.data)
            curr=curr.next
    def ispalindrome(self):
        a=[]
        curr=self.head
        while(curr):
            a.append(curr.data)
            curr=curr.next
            
            
        if(a==a[::-1]):
            print("palindrome")
        else:
            print("not a palindrome")
ll=linkedlist()
ll.append("1")
ll.append("7")
ll.append("3")
ll.append("2")
ll.append("1")
ll.ispalindrome()

                  
    
        
