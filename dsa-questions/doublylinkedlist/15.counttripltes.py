class Solution:
	def trippleSumInLinkedList(self, head,sumv):
		res = []
		s,m,e = head,head,head
		while e.next != None:
			e = e.next
		while s.next.next != None:
			currSum = sumv-s.data
			m = s.next
			ev = e
			while m and ev and m != ev:
				newSum = m.data + ev.data
				if newSum == currSum:
					res.append([s.data,m.data,ev.data])
					m = m.next
				elif newSum > currSum:
					ev = ev.prev
				else:
					m= m.next
			s = s.next
		return res
sol = Solution()

head = Node(1)
node2 = Node(2)
node3 = Node(4)
node4 = Node(5)
node5 = Node(6)
node6 = Node(8)
node7 = Node(9)

head.next = node2
node2.prev = head
node2.next= node3

node3.prev = node2
node3.next = node4

node4.next= node5
node4.prev = node3

node5.prev = node4
node5.next = node6

node6.prev = node5
node6.next = node7

node7.prev= node6


print('solution: ',sol.trippleSumInLinkedList(head,15))
