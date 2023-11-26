#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        
        # code here 
        j = n-1
        i = 0
        m = -1
        l = -1
        v = -1
        while i<n:
            if arr[i] == x:
                m = i
                break
            else:
                i+=1
        while j>= 0:
            if arr[j] == x:
                l = j
                break
            else:
                j-=1
        if m==-1:
            return v,v
        else:
            return m,l
                


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends