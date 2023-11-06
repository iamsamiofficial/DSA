class Solution():

    def checkRedundancy(self, s):
        stack = []
        
        for i in s:
            if i == ")":
                top = stack.pop()
                flag = 1
                while top != '(':
                    if top == "+" or top == "*" or top == "-" or top == "/":
                        flag = 0
                        top = stack.pop()
                    else:
                        top = stack.pop()
                    
                if flag == 1:
                    return 1
            else:
                stack.append(i)
        else:
            return 0


#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        print(Solution().checkRedundancy(s))

# } Driver Code Ends