class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        vals = self.head
        lilist = "["
        while (vals):
            lilist += str(vals.data) + " "
            vals = vals.next
        if (len(lilist) > 2):
            lilist = lilist[:-1]
            lilist += "]"
        print(lilist)

    def insert(self, val):
        if (self.head == None):
            self.head = Node(val)
        else:
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = Node(val)

    def delete(self, ind=0):
        if (ind == 0 and self.head != None):
            temp = self.head
            self.head = temp.next
        elif (ind != 0 and self.head != None):
            temp = self.head
            for a in range(ind):
                prev = temp
                temp = temp.next
            prev.next = temp.next

a = SinglyLinkedList()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)

a.printlist()# prints singly linked list
a.delete() # deletes first node at beginning
a.printlist()
a.delete(2) # deletes node at index 2
a.printlist()
