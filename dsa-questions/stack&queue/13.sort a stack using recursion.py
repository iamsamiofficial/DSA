class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        if s:
            temp = s.pop()
            self.Sorted(s)
            self.insertatbottom(s,temp)
    def insertatbottom(self,s,temp):
        if len(s) == 0 or s[-1] <= temp:
            s.append(temp)
        else:
            sam = s.pop()
            self.insertatbottom(s,temp)
            s.append(sam)
        return s
            



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends