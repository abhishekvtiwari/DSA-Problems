class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class LinkedList:
  def __init__(self):
    self.head=None
    self.c=0


  def add_element(self,data):
    self.c=0
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
      return
    current=self.head
    while current.next:
      self.c+=1
      current=current.next
    current.next=new_node

  def rotate_by(self):
    temp=Node(0)
    sec_last=self.head
    while sec_last.next.next:
      sec_last=sec_last.next
    temp=sec_last.next
    sec_last.next=None
    temp.next=self.head
    self.head=temp
  def Print(self):
    current=self.head
    while current:
      print(current.data)
      current=current.next
# I Love You
a=[1, 4, 6, 8, 7]
b=LinkedList()
for i in a:
  b.add_element(i)

b.rotate_by()
b.Print()
