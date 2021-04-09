class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next= new_node

    def Print(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

    def Detect_Loop(self):
      s=[]
      current=self.head
      while current:
        if current.data in s: 
          return s
        s.append(current.data)
        current=current.next
      return None

a = LinkedList()
a.append(20)
a.append(4)
a.append(15)
a.append(10)
a.append(18)
a.append(19)
a.head.next.next.next.next = a.head
# a.Print()
print(a.Detect_Loop())
# a.Print()
