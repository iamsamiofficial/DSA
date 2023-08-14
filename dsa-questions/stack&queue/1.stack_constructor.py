class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.lenght = 1
stack = Stack(5)


print('Top:',stack.top.value)
print('Height:',stack.lenght)