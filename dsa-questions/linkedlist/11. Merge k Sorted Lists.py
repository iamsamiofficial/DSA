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
    
    #Merging K sorted Lists
    def mergeklists(self,lists):
        if not lists or len(lists) == 0:
            return None
        
        while len(lists)>1:
            mergelist = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergelist.append(self.mergeList(l1,l2))
            lists = mergelist
        return lists[0]
    def mergeList(self,l1,l2):
        dummy = LinkedList(0)
        tail = dummy

        while l1 and l2:
            if l1.value < l2.vale:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next
        

list1 =LinkedList(1)
list1.append(4)
list1.append(5)
list2 =LinkedList(1)
list2.append(3)
list2.append(4)
list3 =LinkedList(2)
list3.append(6)
lists = []
lists.append(list1)
lists.append(list2)
lists.append(list3)


mergeklist = LinkedList(0)
print(mergeklist.mergeklists(lists))


