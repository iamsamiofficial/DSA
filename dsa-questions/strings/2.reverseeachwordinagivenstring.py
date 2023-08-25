#User function Template for python3

class Solution:
    def reverseWords(self, s):
        # code here
        string = s.split('.')
        string1 = ""
        for i in range(len(string)):
            string1 += string[i][::-1]
            string1+='.' if i <len(string)-1 else ""
        return string1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver Code Ends