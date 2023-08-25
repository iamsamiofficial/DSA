# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        s = ""
        # code here
        string = S.split('.')
        
        for i in range(len(string)-1,0,-1):
            s+= string[i]
            s+="."
        s+=string[0]
        return s

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends