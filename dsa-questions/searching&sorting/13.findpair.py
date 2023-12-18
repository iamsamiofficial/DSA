# #User function Template for python3

# class Solution:

#     def findPair(self, arr, L,N): #2 3 5 5 20 80 N = 78
#         #code here
#         dic = {}
        
#         a = set(arr)
#         if len(a) != len(arr) and N==0:
#             return True
#         elif len(a) == len(arr) and N==0:
#             return False
        
#         for i in arr:
#             dic[i] = 1
        
#         for i in arr:
#             if i+N in dic:
#                 return True
#         return False
# #{ 
#  # Driver Code Starts
# #Initial Template for Python 3

# if __name__ == '__main__':

#     t = int(input())

#     for _ in range(t):
#         L,N = [int(x) for x in input().split()]
#         arr = [int(x) for x in input().split()]

#         solObj = Solution()

#         if(solObj.findPair(arr,L, N)):
#             print(1)
#         else:
#             print(-1)
# # } Driver Code Ends

#User function Template for python3

class Solution:

    def findPair(self, arr, L,N): # 10 45 50              n = 30
        #code here
        
        arr = sorted(arr)
        i = 0
        j = 1
        while (i<len(arr) and j<len(arr)):
            
            if (i!=j and arr[j]-arr[i] == N):
                return True
            elif (arr[j]-arr[i] <N):
                j+=1
            else:
                i+=1
        return False
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        L,N = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        if(solObj.findPair(arr,L, N)):
            print(1)
        else:
            print(-1)
# } Driver Code Ends