class Stack:
    # intializes stack
    def __init__(self):
        self.stack = []

    # inserts new element
    def ins(self, item):
        self.stack.append(item)

    # pops out last element
    def lifo(self):
        return self.stack.pop()

    # returns size of stack
    def size(self):
        return len(self.stack)

open_b = Stack()
brackets = input("Please enter parenthesis sequence: ")
reverse_pop = 0

for a in range(len(brackets)):
    # keeps track of closing brackets that appear before opening counterparts
    if open_b.size() == 0 and brackets[a] == ")":
        reverse_pop += 1
    # adds opening brackets to stack
    elif brackets[a] == "(":
        open_b.ins(brackets[a])
    # removes opening bracket from stack when closing is encountered
    elif brackets[a] == ")":
        open_b.lifo()

# checks if stack is empty
if open_b.size()-reverse_pop != 0:
    balanced = False
    print(balanced)
else:
    balanced = True
    print(balanced)
