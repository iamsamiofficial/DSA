#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        i = 0
        count = 0
        maxi = 0
        if max(arr)<0:
            maxi = max(arr)
        else:
            while i <len(arr):
                if (count+arr[i])>0:
                    count+=arr[i]
                    maxi = max(count,maxi)
                    i+=1
                    
                else:
                    count = 0
                    maxi = max(count,maxi)
                    i+=1
                
                
                
                
                
                
            
            
        
        return maxi




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends