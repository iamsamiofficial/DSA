class Solution:
    def findSum(self,A,N): 
        #code here
        mini = 9999999999
        maxi = -99999999
        for i in A:
            if i < mini:
                mini = i
            if i >maxi:
                maxi = i
        summ = mini+maxi
        return summ



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends