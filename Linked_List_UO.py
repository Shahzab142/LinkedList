class Node:
    def __init__(self , item = None):
        self.data = item
        self.Next = None

class LinkedList:
    def __init__(self):
        self.Head = None

    def insert_at_start (self , item):
        New_Node = Node(item)
        New_Node.Next = self.Head
        self.Head = New_Node

    def insert_at_end(self , item ):
        New_Node = Node(item)
        if self.Head == None:
            self.Head = New_Node
            return
        current = self.Head
        while current.Next:
            current = current.Next

        current.Next = New_Node

    def Treverse (self):
        current = self.Head
        while current:
            print(current.data , end = '-->')
            current = current.Next

    def insert_before(self , key , item):
        New_Node = Node(item)
        if self.Head is None:
            print("List is Empty")
            return
        if key==self.Head.data:
            New_Node.Next = self.Head
            return
        pre = self.Head
        cur = self.Head
        while cur and cur.data != key:
            pre = cur
            cur = cur.Next
        if cur and cur.data == key:
            New_Node.Next = cur
            pre.Next = New_Node
        else:
            print("Key Not Found")

    def insert_after(self , key , item):
        New_Node = Node(item)
        current = self.Head
        while current:
            if current.data == key:
                New_Node.Next = current.Next
                current.Next = New_Node
                return
            current = current.Next
        else:
            print("Key Not Found")

    def del_at_start(self):
        if self.Head is None:
            print("List is Empty")
            return
        self.Head = self.Head.Next

    def del_at_end(self):
        if self.Head is None:
            print("List is Empty")
            return
        if self.Head.Next is None:
            self.Head = None
            return
        current = self.Head
        while current.Next.Next:
            current = current.Next
        current.Next = None


    def del_before(self, key):
        if self.Head is None or self.Head.data == key:
            print("List is Empty or Key not found")
            return

        if self.Head.Next is not None and self.Head.Next.data == key:
            self.Head = self.Head.Next
            return

        pre = self.Head
        cur = self.Head.Next

        while cur and cur.Next and cur.Next.data != key:
            pre = cur
            cur = cur.Next

        if cur and cur.Next and cur.Next.data == key:
            pre.Next = cur.Next
        else:
            print("Key Not Found")

    def del_after(self, key):
        if self.Head is None:
            print("List is Empty")
            return

        current = self.Head

        while current and current.data != key:
            current = current.Next

        if current and current.Next:
            current.Next = current.Next.Next
        else:
            print("Key Not Found")

    def del_by_value(self,key):
        if self.Head is None:
            print("List is empty")
            return
        if self.Head.data == key:
            self.Head = self.Head.Next
            return
        pre = self.Head
        cur = self.Head
        while cur and cur.data != key:
            pre = cur
            cur = cur.Next
        if cur:
            pre.Next = cur.Next
        else:
            print("Key Not Found")

    def reverse(self):
        prev = None
        current = self.Head

        while current:
            next_node = current.Next
            current.Next = prev
            prev = current
            current = next_node

        self.Head = prev


MyList = LinkedList()
MyList.insert_at_start(30)
MyList.insert_at_start(20)
MyList.insert_at_start(10)
MyList.insert_at_end(40)
MyList.insert_at_end(50)
MyList.insert_before(50,45)
MyList.insert_after(50,60)
MyList.insert_after(60,70)
MyList.del_at_start()
MyList.Treverse()
print("\n")
MyList.del_by_value(70)
MyList.Treverse()
print("\n")
MyList.del_before(50)
MyList.Treverse()
print("\n")
MyList.del_after(40)
MyList.Treverse()



