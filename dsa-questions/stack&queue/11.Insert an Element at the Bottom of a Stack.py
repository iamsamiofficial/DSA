#User function Template for python3
class Solution:
    def insertAtBottom(self,St,X):
        # code here
        new = []
        while St:
            new.append(St.pop())
        St.append(X)
        while new:
            St.append(new.pop())
        return St

#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        n,x = map(int,input().split())
        stack = list(map(int,input().split()))
        obj = Solution()
        ans = obj.insertAtBottom(stack,x)
        for e in ans:
            print(e,end=" ")
        print()
        
        
        
# } Driver Code Ends