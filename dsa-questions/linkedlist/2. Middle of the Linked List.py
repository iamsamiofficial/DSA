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
    
    

    #finding the middle node of the linkded list without using the len method

    def middle(self):
        before = self.head
        after = self.head
        while after is not None and after.next is not None:
            before = before.next
            after = after.next.next
        return before



        






middle = LinkedList(1)
middle.append(2)
middle.append(3)
middle.append(4)
middle.printList()
print(middle.middle().value)









        

