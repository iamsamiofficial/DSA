class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.lenght = 1

    def push(self,value):#prependmethod
        new_node = Node(value)
        if self.lenght == 0:
            self.top = new_node
        
        else:
            new_node.next = self.top
            self.top = new_node
        self.lenght +=1
        return True

    def pop(self):#popfirstmethod
        if self.lenght == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.lenght -=1
        return temp
    
    def printstack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
stack = Stack(5)
stack.push(4)
stack.printstack()

print('after pop')
print(stack.pop().value)
stack.printstack()


