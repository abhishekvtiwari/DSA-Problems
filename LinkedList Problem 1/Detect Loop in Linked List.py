# A single node of a single linked list
class Node:
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  def append(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
        self.head = new_node
        return

    last = self.head
    while (last.next is not None):
      last = last.next

    last.next = new_node
  
  def printLL(self):
    current = self.head
    while(current):
      print(current.data, end='=>')
      current = current.next

if __name__=='__main__':
  llist = LinkedList()
  llist.append(20)
  llist.append(4)
  llist.append(15)
  llist.append(10)
  llist.printLL()
    
