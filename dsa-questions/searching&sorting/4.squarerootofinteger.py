#User function Template for python3

class Solution:
    def countSquares(self, N):
        store = math.sqrt(N)
        if store == int(store):
            return int(store-1)
        else:
            return int(store)
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends