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
    def partition_list(self,k):
        dummy1 = Node(0)
        dummy2 = Node(0)
        pre1 = dummy1
        pre2 = dummy2
        pre1.next = self.head
        pre2.next = self.head
        current = self.head

        while current:
            if current.value < k:
                pre1.next = current
                pre1 = current
            else:
                pre2.next = current
                pre2 = current
            current = current.next
        pre1.next = dummy2.next
        pre2.next = None
        ans = dummy1.next





remove_dup = LinkedList(1)
remove_dup.append(4)
remove_dup.append(3)
remove_dup.append(2)
remove_dup.append(5)
remove_dup.append(2)
remove_dup.printList()
remove_dup.partition_list(3)
print('after partitioning list')
remove_dup.printList()

