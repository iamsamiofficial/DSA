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
    
    #reversing the linked list 1 4 3 2 5 2
    def reverse_list(self):
        temp = self.head                            
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        while after:
            after = after.next
            temp.next = before
            before = temp
            
            temp = after
            


# while after:
#         after = after.next
#         temp.next = before
#         before = temp
#         temp = after


remove_dup = LinkedList(1)
remove_dup.append(4)
remove_dup.append(3)
remove_dup.append(2)
remove_dup.append(5)
remove_dup.append(2)
remove_dup.printList()
remove_dup.reverse_list()
print('after reversing list')
remove_dup.printList()

