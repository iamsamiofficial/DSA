#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def reverse(self,value):
        prev = None
        temp = value
        after = temp.next
        
        while temp:
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after
        return prev
        
    
    def addTwoLists(self, first, second):
        # code here
        dummy = LinkedList()
        store = dummy
        l1 = self.reverse(first)
        l2 = self.reverse(second)
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.data if l1 else 0
            v2 = l2.data if l2 else 0
            
            value = v1+v2+carry
            carry = value //10
            v = value % 10
            store.next = Node(v)
            
            store = store.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return self.reverse(dummy.next)
        
        # return head of sum list


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends