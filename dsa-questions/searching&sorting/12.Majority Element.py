#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        dic = {}
        for i in A:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        b = 0
        for key,value in dic.items():
            if value > N/2:
                return key
        return -1
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends