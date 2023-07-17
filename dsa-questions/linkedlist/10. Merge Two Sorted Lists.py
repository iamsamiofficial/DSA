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
    
    def check(self,m1):
        m4 = LinkedList(1)
        if m1.head == m4.head:
            m4 = m1.head
        return m4



    #Merge two sorted list
    def mergelist(self,head1,head2):
        while head1 and head2:
            if head1.value<head2.value:
                m3.append(head1.value)
                print(head1.value)
                head1 = head1.next
            else:
                m3.append(head2.value)
                print(head2.value)
                head2 = head2.next
        while head1:
            m3.append(head1.value)
            head1 = head1.next
        while head2:
            m3.append(head2.value)
            head2 = head2.next
            

        return m3
            


            


m1 = LinkedList(1)
m1.append(2)
m1.append(4)
solve = m1.check(m1)
solve.printList()
print('fiish')
m2 = LinkedList(1)
m2.append(3)
m2.append(4)

m3 = LinkedList(0)
final = m3.mergelist(m1.head,m2.head)
print('after evverything:')
final.printList()

