#User function Template for python3

from typing import List
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def insertbottom(self,St,n):
        if len(St) == 0:
            St.append(n)
        else:
            t = St.pop()
           
            self.insertbottom(St,n)
            St.append(t)
    def reverse(self,St):
        if St:
            y = St.pop()
            self.reverse(St)
            self.insertbottom(St,y)
        return St
        
    

        
        
        


#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends