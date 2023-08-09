class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class Doublylinkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True

    def pop(self):
        if self.length == 0:
            return  None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -=1
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1
        return True
    
    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -=1
        return temp

    def get(self,index):
        
        if index < 0 or index>= self.length:
            return None
        
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
        return temp

    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # def insert(self,index,value):
    #     new_node = Node(value)
    #     temp = self.get(index)
    #     temp.prev.next = new_node
    #     new_node.prev = temp.prev
    #     new_node.next = temp
    #     temp.prev = new_node
    #     self.length+=1

    def insert(self,index,value):
        if index<0 or index>= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        before = self.get(index-1)
        after = before.next
        new_node = Node(value)

        new_node.prev = before
        before.next = new_node
        new_node.next = after
        after.prev = new_node
        self.length +=1
        return True
    
    def remove(self,index):
        if index <0 or index >=self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -=1
        return temp

    def reverse(self): #1 2 3 4 4 3 2 1
        temp = self.head
        while temp:
            temp.prev,temp.next = temp.next,temp.prev
            temp = temp.prev
        self.head,self.tail = self.tail,self.head
    
    def palindrome(self):
        if self.length <=1:
            return True
        forward = self.head
        backword = self.tail
        # i = 0
        # j = self.length-1
        # while i<j:
        #     if forward.value != backword.value:
        #         return False
        #     forward = forward.next
        #     backword = backword.prev
        #     i+=1
        #     j-=1
        # return True

        for _ in range(self.length//2):
            if forward.value != backword.value:
                return False
            forward = forward.next
            backword = backword.prev
        return True

    

    def swapnodes(self): #1 2 3 4 2 1
        # temp = self.head
        # while temp and temp.next:
        #     temp.value,temp.next.value = temp.next.value,temp.value
        #     temp = temp.next.next
        temp = self.head
        sam = self.head
        if self.head is None:
            return None
        if self.head.next is None:
            return self.head
        while temp:
            temp.next = temp.next.next
            temp = temp.next
            temp.next = self.head
            



doubly = Doublylinkedlist(1)
doubly.append(2)
doubly.append(3)
doubly.append(4)

doubly.swapnodes()

doubly.printlist()


