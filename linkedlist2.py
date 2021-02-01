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

    def search(self, val):
        temp = self.head
        while (temp):
            if (str(temp.data) == str(val)):
                return True
            else:
                temp = temp.next
        return False

    def reverse(self):
        rvrsd = None
        temp = self.head
        while (temp):
            next = temp.next
            temp.next = rvrsd
            rvrsd = temp
            temp = next
        self.head = rvrsd

a = SinglyLinkedList()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)

a.printlist()

print(a.search(0))
print(a.search(1))
print(a.search(22))
print(a.search(4))

a.reverse()
a.printlist()
