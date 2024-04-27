class Node:
      def __init__(self, data):    #constructor--to intilze the variables when oject is creted
          self.data =  data
          self.next = None     #adddress of next node
        
        
class linkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print('Linked List is empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
      
L=linkedList()
n=Node(10)




L.head=n
n1=Node(20)
L.head.next=n1
n2=Node(30)
n1.next=n2
L.display()
       
    
    
