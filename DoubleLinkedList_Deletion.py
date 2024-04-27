class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print("Empty Double Linked List")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->", end=" ")
                temp= temp.next
    def delete_begining(self,data):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None
    def delete_end(self,data):
        temp=self.head.next
        before=self.head
        while temp.next is not None:
            temp=temp.next
            before=before.next
        before.next=None
        temp.prev=None
    def delete_position(self,pos):
        temp=self.head.next
        before=self.head
        for i in range(1,pos-1):
            temp=temp.next
            before=before.next
        before.next=temp.next
        temp.next.prev=before
        temp.next=None
        temp.prev=None
        
            
        
        
                
                
L=DLL()
#L.display()
n1=Node(10)
L.head=n1



n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n3.prev=n2
n2.next=n3
n4=Node(40)
n4.prev=n3
n3.next=n4
n4=Node(40)
n4.prev=n3
n5=Node(50)
n5.prev=n4
n4.next=n5
#L.insert_beginning(7)
#L.insert_beginning(5)
#L.insert_end(50)
#L.insert_position(3, 25)

L.delete_begining(1)
L#.delete_end(40)
#L.delete_position(3)
L.display()



