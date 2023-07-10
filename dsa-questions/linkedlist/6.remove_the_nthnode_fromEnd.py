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
    
    #removing the kth node of a linked list from the last
    def removing_kNode(self,k):
        slow = self.head
        fast = self.head
        pre = None
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            pre = slow
            slow = slow.next
            fast = fast.next
        pre.next = slow.next
        return True
        




remove_dup = LinkedList(1)
remove_dup.append(2)
remove_dup.append(3)
remove_dup.append(1)
remove_dup.append(4)
remove_dup.append(2)
remove_dup.append(5)
remove_dup.printList()
remove_dup.removing_kNode(3)
print('after removing k node')
remove_dup.printList()

