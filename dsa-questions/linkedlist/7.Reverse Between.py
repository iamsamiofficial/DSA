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
    
    #reversing two nodes from the linked list 
    def reversing_kNode(self,m,n):
        if not self.head:
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for _ in range(m):
            prev = prev.next
        current = prev.next
        for _ in range(n-m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        self.head = dummy.next
        return self.head
        # onenode = self.head
        # prevone = None
        # twonode = self.head
        # prevtwo = None
        # for _ in range(m):
        #     if onenode is None:
        #         return None
        #     prevone = onenode
        #     onenode = onenode.next
       
        # for _ in range (n):
        #     if twonode is None:
        #         return None
        #     prevtwo = twonode
        #     twonode = twonode.next
        # prevone.next = twonode
        # store = twonode.next
        # twonode.next = onenode.next
        # prevtwo.next = onenode
        # onenode.next = store
        # return True



#  temp = current.next
#            current.next = temp.next
#             temp.next = prev.next
#             prev.next = temp

remove_dup = LinkedList(1)            
remove_dup.append(2)
remove_dup.append(3)
remove_dup.append(4)
remove_dup.append(5)
remove_dup.printList()
remove_dup.reversing_kNode(3,4)
print('after swapping:')
remove_dup.printList()

