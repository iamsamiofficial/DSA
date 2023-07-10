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
    def removeduplicates(self):
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
    
    #removing duplicates from the linked list with O(n)
    def remove_duplicates(self):
        values = set()
        current = self.head
        pre = None

        while current:
            if current.value in values:
                pre.next = current.next
                current = pre.next
                self.length -=1
            else:
                values.add(current.value)
                pre = current
                current = current.next
        return values



remove_dup = LinkedList(1)
remove_dup.append(2)
remove_dup.append(3)
remove_dup.append(1)
remove_dup.append(4)
remove_dup.append(2)
remove_dup.append(5)
remove_dup.printList()
print(remove_dup.remove_duplicates())
print('removing duplicates')
remove_dup.printList()











        

