#User function Template for python3

class Solution:
    def findMin(self, arr, n):
        #complete the function here
        
        l = 0
        h = len(arr)-1
        res = arr[0]
        while l<=h:
            
            if arr[l]<=arr[h]:
                res = min(res,arr[l])
                break
            m = (l+h)//2
            res = min(res,arr[m])
            if arr[m] >= arr[l]:
                l = m+1
            else:
                h = m-1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends