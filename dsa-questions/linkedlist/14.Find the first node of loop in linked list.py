class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

                                        #LECTURER IN METRO 
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    #printing the llinkedist
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    #Appending node in a linkedlist time complexity O(1)
    def append(self,value):
        new_node = Node(value)
        
        if self.length is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
        return True
    
    #Popping node from a linked list time complexity O(N)
    def pop(self):
        if self.length == 0:
            return False
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    #prepending node in a linkedlist time complexity of O(1)
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True

    #popping the first node from the linkedlist time complexity o(1)
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        temp.next = None
        self.head = self.head.next
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp

    #getting a node from the linkedlist time complexity O(n)
    def get(self,index):
        if index<0 or index>= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    #setting a value in linkedlist time complextiy O(n)
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    #inserting a node in linkedlist
    def insert(self,index,value):
        if index<0 or index>= self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    #removing a node from the linkedlist
    def remove(self,index):
        if index<0 or index>= self.length:
            return None
        if index == 0:
            return self.pop_first
        if index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp

    #reversing a linkedlist
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    #palindorom check

    def palindrome(self):
        temp = self.head
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        after = slow.next
        while slow:
            after = slow.next
            slow.next = prev
            prev = slow
            slow = after

        while prev:
            if temp.value != prev.value:
                return False
            temp = temp.next
            prev = prev.next
        return True

       #Function to find first node if the linked list has a loop.
    def findFirstNode(self, head):
        #code here
        temp = head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast is None:
            return -1
        while slow != temp:
            temp = temp.next
            slow = slow.next
        return slow.data



        






ex1 = LinkedList(1)
ex1.append(2)
ex1.append(3)
ex1.append(2)
ex1.append(1)
ex1.printList()
print(ex1.palindrome())








        

