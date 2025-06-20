class Node :
    def __init__(self , data = None):
        self.data = data
        self.next = None

class linkedlist :
    def __init__ (self):
        self.head = Node()

    def accept_data (self , data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:

            cur = cur.next
        cur.next = new_node

    def display (self):
        disp = []
        cur = self.head

        while cur.next != None:
            cur = cur.next
            disp.append (cur.data)

        print(disp)

l = linkedlist ()
l.accept_data(1)
l.accept_data(2)
l.accept_data(3)
l.accept_data(4)
l.accept_data(5)

l.display()

