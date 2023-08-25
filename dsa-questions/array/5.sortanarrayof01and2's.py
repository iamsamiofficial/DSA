#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        l = 0
        mid = 0
        h = n-1
        
        for i in range(n):
            if arr[mid] == 0:
                arr[l],arr[mid] = arr[mid],arr[l]
                mid+=1
                l+=1
            elif arr[mid] == 1:
                mid+=1
            else:
                arr[h],arr[mid] = arr[mid],arr[h]
                h-=1
        return arr
                
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends