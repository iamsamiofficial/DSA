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

    #removing duplicates from the linked list with O(n^2)
    def remove_duplicates(self):
        current = self.head
        while(current):
            runner = current
            while runner.next:
                if current.value == runner.next.value:
                    runner.next = runner.next.next
                    self.length -=1
                else:
                    runner = runner.next
            current = current.next
        return True


remove_dup = LinkedList(1)
remove_dup.append(2)
remove_dup.append(3)
remove_dup.append(1)
remove_dup.append(4)
remove_dup.append(2)
remove_dup.append(5)
remove_dup.printList()
remove_dup.remove_duplicates()
print('removing duplicates')
remove_dup.printList()











        

